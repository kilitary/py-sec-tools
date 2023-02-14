#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L
import os.path
import random
import secrets
import sys
from enum import Enum, auto
from var_dump import var_dump
from helpers import deb
from pprint import pprint
from outputdebugstring import olog
from randomer import Randomer
import argparse
import base64

assembled = []
labels = {}
allowed = []
operands_stat = {}

class Operand(Enum):
    LABEL = auto()
    SET = auto()
    PLAIN = auto()
    SETV = auto()
    COLOR = auto()
    GOTO = auto()
    TITLE = auto()
    ECHO = auto()
    CALL = auto()
    REM = auto()
    EXIT = auto()
    DISALLOWED = auto()

def write(filename: str, code: str) -> None:
    with open(filename, "w") as file:
        file.write("@ECHO ===========================================================\n")
        ret = file.write(code)
        deb(f'\nwritten {ret} bytes ({len(assembled)} commands) to {filename}\r\n')

def get_unused_label(min_i=0):
    try:
        lst = []
        for label, used in labels.items():
            if used == 0:
                lst.append(label)
        random.shuffle(lst)
        s = lst[random.randint(0, len(lst) - 1)]
        return s
    except Exception as e:
        print(f'error: {e}')

def mark_used_label(label):
    try:
        labels[label] += 1
    except Exception as e:
        print(f'exception({label}): {e}')

def get_unlinked_label_index():
    try:
        lst = []
        for label, used in labels.items():
            if used == 1:
                for ai in range(0, len(assembled)):
                    if assembled[ai][0] == Operand.LABEL and assembled[ai][1] == label:
                        labels[label] += 1
                        return ai
        return 0
    except Exception as e:
        print(f'error: {e}')

def setup_allowed():
    allowed.append(Operand.GOTO)
    allowed.append(Operand.SET)
    allowed.append(Operand.ECHO)
    allowed.append(Operand.TITLE)
    allowed.append(Operand.COLOR)
    allowed.append(Operand.REM)
    # allowed.append(Operand.CALL)

def get_random_index():
    ai_offset = random.randint(1, len(assembled) - 1)
    return ai_offset

def hexify_data(data: str) -> str:
    cur_row = 0
    code = '::: '
    for i in range(0, len(data)):
        c = hex(data[i])[2:]
        c = f'{int(c, base=16):02x}'
        if cur_row > 15:
            c += "\n:::"
            cur_row = 0
        else:
            cur_row += 1
        code += c + " "
    code += "\n"
    return code

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default='', help="embedded file")
    parser.add_argument("-m", "--max", type=int, default=1000, help="max instructions")
    args = parser.parse_args()
    
    if args.file:
        size = os.path.getsize(args.file)
        print(f'embedding {args.file} size: {size / 1024.0 / 1024.0:.2f} Mbytes')
        
        with open(args.file, "rb") as file:
            embeddedData = file.read()
            base64encodedData = str(base64.b64encode(embeddedData).decode('utf-8'))
            # base64encodedData = base64encodedData.replace('A', 'C')
            print(f'base64 size: {len(base64encodedData) / 1024.0 / 1024.0:.2f} Mbytes')
    else:
        print(f'blackhole mode')
    
    setup_allowed()
    num_instructions = random.randint(13, args.max)
    
    # Generate lables
    cur_i = 0
    print(f'generating labels ...', end='', flush=True)
    for n_label in range(0, num_instructions - 1):
        label = Randomer.str_generator()
        labels[label] = 0
        assembled.append([Operand.LABEL, label])
        cur_i += 1
        print(f'\rgenerating labels ... {cur_i / (num_instructions - 1) * 100.0:.2f}%', end="", flush=True)
    
    # Use labels
    print(f"\nconnecting labels ... ", end='', flush=True)
    cur_i = 0
    for n_instruction in range(0, num_instructions):
        # find next allowed function
        instruction_type = Operand.DISALLOWED
        while instruction_type not in allowed:
            instruction_type = Operand(random.randint(1, len(Operand) - 1))
        
        # operands loop
        if instruction_type == Operand.GOTO:
            lbl = get_unused_label()
            if lbl == None:
                break
            ai_offset = get_unlinked_label_index()
            assembled.insert(ai_offset, [Operand.GOTO, lbl])
            mark_used_label(lbl)
        
        if instruction_type == Operand.CALL:
            lbl = get_unused_label()
            if lbl == None:
                break
            ai_offset = get_unlinked_label_index()
            assembled.insert(ai_offset, [Operand.CALL, lbl])
            mark_used_label(lbl)
        
        if instruction_type == Operand.SET:
            op1 = Randomer.str_id_generator(size=random.randint(5, 10))
            op2 = Randomer.str_id_generator(size=random.randint(10, 40))
            op = op1 + '=' + op2
            ai_offset = get_random_index()
            assembled.insert(ai_offset, [Operand.SET, op])
        
        if instruction_type == Operand.SETV:
            pass
        
        if instruction_type == Operand.TITLE:
            op2 = Randomer.str_str_generator(size=random.randint(14, 50))
            ai_offset = get_random_index()
            assembled.insert(ai_offset, [Operand.TITLE, op2])
        
        if instruction_type == Operand.ECHO:
            op = Randomer.str_str_generator(size=random.randint(2, 55))
            ai_offset = get_random_index()
            assembled.insert(ai_offset, [Operand.ECHO, op])
        
        if instruction_type == Operand.REM:
            op = Randomer.str_str_generator(size=random.randint(2, 55))
            ai_offset = get_random_index()
            assembled.insert(ai_offset, [Operand.REM, op])
        
        if instruction_type == Operand.COLOR:
            op1 = hex(random.randint(0, 0xf))[2:]
            op2 = hex(random.randint(0, 0xf))[2:]
            op = op1 + op2
            ai_offset = get_random_index()
            assembled.insert(ai_offset, [Operand.COLOR, op])
        
        if instruction_type == Operand.CALL:
            pass
        
        # save op's stats
        try:
            operands_stat[instruction_type] += 1
        except:
            operands_stat[instruction_type] = 1
        
        # show what
        cur_i += 1
        print(f'\rconnecting labels ... {cur_i / num_instructions * 100.0:.2f}%', end="", flush=True)
    
    if embeddedData != None:
        pre = f"@echo off\nerase hex.temp\n"
        data = hexify_data(embeddedData)
        post = " > hex.temp (" \
               "for /f \"delims=: tokens=*\" %%A in " \
               "('findstr \"^:::\" \"%~f0\"') do echo %%A" \
               ")"
        decoder = f"\ncertutil -f -decodeHex hex.temp {args.file} >nul\n"
        eraser = "\nerase hex.temp\n"
        executer = f"\n{args.file}"
        body = pre + data + post + decoder + eraser + executer
        assembled.append([Operand.PLAIN, body])
    
    assembled.append([Operand.EXIT, ''])
    
    print(f'\nassembling code ... ', end="")
    
    code = ''
    n_inst = 0
    tot = len(assembled)
    for instruction, data in assembled:
        # print(f'{n_inst:05d} i: {instruction} l: {data}')
        if instruction == Operand.GOTO:
            code += 'goto ' + data + "\n"
        if instruction == Operand.CALL:
            code += 'call :' + data + "\n"
        if instruction == Operand.LABEL:
            code += ':' + data + "\n"
        if instruction == Operand.EXIT:
            code += "echo done!\n"
            code += 'exit'
        if instruction == Operand.SET:
            code += 'set ' + data + "\n"
        if instruction == Operand.TITLE:
            code += 'title ' + data + "\n"
        if instruction == Operand.ECHO:
            code += 'echo ' + data + "\n"
        if instruction == Operand.REM:
            code += 'rem ' + data + "\n"
        if instruction == Operand.COLOR:
            code += 'color ' + data + "\n"
        if instruction == Operand.PLAIN:
            code += data + "\n"
        n_inst += 1
        print(f'\rassembling code ... {n_inst / tot * 100.0:.2f}%', end='')
    
    write('mut.cmd', code)
    
    pprint(operands_stat, indent=4, compact=True)
