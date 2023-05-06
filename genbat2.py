#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L
import os.path
import random
import secrets
import sys
from enum import Enum, auto
from helpers import deb
from pprint import pprint
from outputdebugstring import olog
from randomer import Randomer
import argparse
import base64, time
import ctypes
import win32api, win32con
import tqdm

assembled = []
labels = {}
allowed = []

operands_stat = {}
debug_trace = False
blackhole = False

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
    """
    Writes the given code to the specified file.

    Args:
        filename (str): The name of the file to write to.
        code (str): The code to write to the file.
    """
    with open(filename, "w") as file:
        file.write("@ECHO ===========================================================\n")
        ret = file.write(code)
        deb(f'\nwritten {ret} bytes ({len(assembled)} commands, ~{(len(assembled) * 0.2) / 1000:7.2f}mins) to {filename}\r\n')

# def get_unused_label(min_i=0):
#     try:
#         lst = []
#         for label, used in labels.items():
#             if used == 0:
#                 lst.append(label)
#         random.shuffle(lst)
#         s = lst[random.randint(0, len(lst) - 1)]
#         return s
#     except Exception as e:
#         print(f'error: {e}')

# def get_unused_label() -> str:
#     unused_labels = [label for label, used in labels.items() if not used]
#     if unused_labels:
#         return random.choice(unused_labels)
#     else:
#         return None

def get_unused_label() -> str:
    unused_labels = [label for label, used in labels.items() if not used]
    return random.choice(unused_labels) if unused_labels else None

def mark_used_label(label):
    """
    Increments the count of the given label in the 'labels' dictionary.

    """
    labels[label] = labels.get(label, 0) + 1

# def get_unlinked_label_index():
#     try:
#         lst = []
#         for label, used in labels.items():
#             if used == 1:
#                 for ai in range(0, len(assembled)):
#                     if assembled[ai][0] == Operand.LABEL and assembled[ai][1] == label:
#                         labels[label] += 1
#                         return ai
#         return 0
#     except Exception as e:
#         print(f'error: {e}')

def get_unlinked_label_index():
    """
    Finds the index of the first unlinked label in the assembled code.
    Returns:
        int: The index of the first unlinked label in the assembled code. If no unlinked label is found, returns 0.
    """
    for i, (label, used) in enumerate(labels.items()):
        if used == 1:
            for j in range(len(assembled)):
                if assembled[j][0] == Operand.LABEL and assembled[j][1] == label:
                    labels[label] += 1
                    return j
    return 0

def setup_allowed():
    """
    Adds a list of allowed operands to the global 'allowed' list.

    """
    allowed.append(Operand.GOTO)
    allowed.append(Operand.SET)
    allowed.append(Operand.ECHO)
    allowed.append(Operand.TITLE)
    allowed.append(Operand.COLOR)
    allowed.append(Operand.REM)
    # allowed.append(Operand.CALL)

def get_random_index():
    """
    Returns a random index within the range of the 'assembled' list.

    :return: A random integer index within the range of the 'assembled' list.
    :rtype: int
    """
    ai_offset = random.randint(1, len(assembled) - 1)
    return ai_offset

def hexify_data(data: str) -> str:
    """
    Converts the input string into a hexadecimal format with a maximum of 16 characters per row.

    Args:
    - data (str): The input string to be converted into hexadecimal format.

    """
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

# def check_assembled():
#     """
#     Checks for code overlap in the assembled code.
#
#     :return: None
#     """
#     global assembled
#
#     error = False
#     print(f'\nchecking code overlap ... ', end='')
#     visited_lables = []
#     for i, d in assembled:
#         if i == Operand.GOTO:
#             if d in visited_lables:
#                 print(f'jmp {d} looped')
#                 error = True
#             else:
#                 visited_lables.append(d)
#     if error:
#         print(f'FAIL')
#         sys.exit(-1)
#     else:
#         print(f'OK')

def check_assembled():
    """
    Checks for code overlap in the assembled code.
    """
    global assembled
    
    error = False
    visited_labels = set()
    label_visit_count = {}
    print('\r\nchecking code overlap ... ', end='')
    for op, item in assembled:
        if op == Operand.GOTO:
            if item in visited_labels:
                print(f'jmp {item} looped')
                error = True
                break
            visited_labels.add(item)
            try:
                label_visit_count[item] = label_visit_count[item] + 1
            except:
                label_visit_count[item] = 1
    
    if error:
        print('FAIL')
        sys.exit(-8)
    
    print('2nd check ... ', end='')
    for op, item in assembled:
        if op == Operand.GOTO:
            if label_visit_count[item] > 1:
                print(f'jmp {item} looped')
                error = True
                break
    
    if error:
        print('FAIL')
        sys.exit(-8)
    else:
        print(f'{len(visited_labels)} JUMPS OK')

def remove_unlinked_labels():
    """
    Removes unused labels from the assembled instructions.

    If blackhole is True, emits a message indicating that not linked instructions will be printed and returns.

    Otherwise, iterates through the labels and their usage. If a label is unused, iterates through the assembled instructions
    to find and remove the corresponding label. If an error occurs during removal, a warning message is printed.

    Prints the number of deleted instructions if any were removed, or a message indicating that none were found.

    :return: None
    """
    global assembled
    if blackhole:
        print(f'emit not linked labels')
        return
    
    print(f'unused instructions check ... ', end='')
    
    deleted = 0
    tot = len(labels)
    processed = 0
    for _, (name, usage) in enumerate(labels.items()):
        print(f'\rremoving unused labels ... {processed / tot * 100.0:.2f}% ' +
              f'({deleted:6d} deleted {deleted / tot * 100.0:.2f}%)', end='')
        if usage == 0:
            for indexj, (i, d) in enumerate(assembled):
                if i == Operand.LABEL and d == name:
                    del assembled[indexj]
                    deleted += 1
        processed += 1
    if deleted:
        print(f'\n{deleted} labels removed')
    else:
        print(f' none found')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default='', help="embedded file")
    parser.add_argument("-d", "--debug", action='store_true', default=False,
                        help="include debug trace", required=False)
    parser.add_argument("-b", "--blackhole", action='store_true', default=False,
                        help="cpu exhaust mode (dont exclude unused instructions)", required=False)
    parser.add_argument("-m", "--max", type=int, default=15000, help="max instructions")
    args = parser.parse_args()
    
    if args.debug:
        debug_trace = True
        print(f'use tracing')
    
    if args.blackhole:
        blackhole = True
        print(f'blackhole mode')
    
    if args.file:
        size = os.path.getsize(args.file)
        print(f'embedding "{args.file}" size: {size / 1024.0 / 1024.0:.2f} Mbytes ({size} bytes)')
        
        with open(args.file, "rb") as file:
            overlayData = file.read()
            base64encodedData = str(base64.b64encode(overlayData).decode('utf-8'))
            size = len(base64encodedData)
            print(f'base64 size: {size / 1024.0 / 1024.0:.2f} Mbytes  ({size} bytes)')
    else:
        print(f'dumb mode')
    
    setup_allowed()
    
    num_instructions = random.randint(args.max * 0.7, args.max)
    print(f'{num_instructions} instructions will be generated')
    
    cur_i = 0
    for n_label in tqdm.tqdm(range(0, num_instructions - 1), desc="generating labels"):
        label = Randomer.str_generator()
        labels[label] = 0
        assembled.append([Operand.LABEL, label])
        cur_i += 1
        # print(f'\rgenerating labels ... {cur_i / (num_instructions - 1) * 100.0:6.2f}%', end="", flush=True)
    
    # Use labels
    # print(f"\nconnecting labels ... ", end='', flush=True)
    cur_i = 0
    for n_instruction in tqdm.tqdm(range(num_instructions), desc="connecting labels"):
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
            if debug_trace:
                op2 = f'(run {cur_i}/{num_instructions}) '
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
        
        # save op's stats
        try:
            operands_stat[instruction_type] += 1
        except:
            operands_stat[instruction_type] = 1
        
        # show what
        cur_i += 1
        # print(f'\rconnecting labels ... {(cur_i / num_instructions) * 100.0:6.2f}%', end="", flush=True)
    
    if overlayData != None:
        pre = f"@echo off\nerase hex.temp p_{args.file}\n"
        data = hexify_data(overlayData)
        post = ">hex.temp (" \
               "for /f \"delims=: tokens=*\" %%A in " \
               "('findstr \"^:::\" \"%~f0\"') do echo %%A" \
               ")"
        decoder = f"\ncertutil -f -decodeHex hex.temp p_{args.file} >nul\n"
        eraser = "\nerase hex.temp\n"
        executer = f"\ncmd /c p_{args.file}\nrem erase p_{args.file}\n"
        body = pre + data + post + decoder + eraser + executer
        assembled.append([Operand.PLAIN, body])
    
    assembled.append([Operand.EXIT, ''])
    
    check_assembled()
    remove_unlinked_labels()
    
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
        print(f'\rassembling code ... {n_inst / tot * 100.0:6.2f}% ', end='')
    
    print(f' done: assembled {n_inst} instructions')
    write('mut.cmd', code)
    
    pprint(operands_stat, indent=2, compact=False)
