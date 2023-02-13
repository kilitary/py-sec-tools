#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

import random
import secrets
import sys
from enum import Enum, auto
from var_dump import var_dump
from helpers import deb
from pprint import pprint
from outputdebugstring import olog
from randomer import Randomer

assembled = []
labels = {}

class Operand(Enum):
    LABEL = auto()
    SET = auto()
    SETV = auto()
    COLOR = auto()
    GOTO = auto()
    TITLE = auto()
    ECHO = auto()
    REM = auto()
    EXIT = auto()

def write(filename: str, code: str) -> None:
    with open(filename, "w") as file:
        file.write("@ECHO ===========================================================\n")
        ret = file.write(code)
        deb(f'\nwritten {ret} bytes to {filename}\r\n')

def get_unused_label(min_i=0):
    try:
        lst = []
        for label, used in labels.items():
            # print(f'label={label} used={used}')
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

def get_ulinked_label_index():
    try:
        lst = []
        for label, used in labels.items():
            # print(f'label={label} used={used}')
            if used == 1:
                for ai in range(0, len(assembled)):
                    if assembled[ai][0] == Operand.LABEL and assembled[ai][1] == label:
                        labels[label] += 1
                        return ai
        return 0
    except Exception as e:
        print(f'error: {e}')

if __name__ == '__main__':
    num_instructions = random.randint(3, 11110)
    allowed = []
    allowed.append(Operand.GOTO)
    
    ''' Generate lables '''
    print(f'generating labels ...')
    for n_label in range(0, num_instructions - 1):
        label = Randomer.str_id_generator()
        labels[label] = 0
        assembled.append([Operand.LABEL, label])
    
    ''' Use labels '''
    print(f'connecting labels ...')
    for n_instruction in range(0, num_instructions):
        while True:
            instruction_type = Operand(random.randint(1, len(Operand) - 1))
            if instruction_type in allowed:
                break
        if instruction_type == Operand.GOTO:
            # lbl = get_unused_label()
            # assembled.append([Operand.GOTO, lbl])
            # mark_used_label(lbl)
            
            lbl = get_unused_label()
            if lbl == None:
                assembled.append([Operand.EXIT, ''])
                break
            ai_offset = get_ulinked_label_index()
            # assembled[ai_offset:ai_offset] = [Operand.GOTO, lbl]
            assembled.insert(ai_offset, [Operand.GOTO, lbl])
            mark_used_label(lbl)

    print(f'assembling code ...')
    code = ''
    n_inst = 0
    for instruction, data in assembled:
        print(f'{n_inst:05d} i: {instruction} l: {data}')
        if instruction == Operand.GOTO:
            code += 'goto ' + data + "\n"
        if instruction == Operand.LABEL:
            code += ':' + data + "\n"
        if instruction == Operand.EXIT:
            code += "echo done!\n"
            code += 'exit'
        n_inst += 1
    
    write('mut.cmd', code)
    
    print(code)
