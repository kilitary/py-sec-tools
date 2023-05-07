# revised
import os
import math
import random
import sys

with open("bsd-patches.tok", 'r', encoding='utf-8') as bsd_pathes_file:
    bsd_file_pathes = bsd_pathes_file.readlines()

def get_pred_tok(allow_dir=True):
    toks = [
        "\\", "%", "'", "?", "/", ".", "!" + str(random.randint(0, 255)), " ",
        "..", "$", "^", "@", "!", "&", "*",
        "(", ")", "-", "=", "+", "|", "[",
        "]", ">", "<", ",", "?", "~", "`", "}", "{", "\"", ";",
        f'%{random.randint(0x01, 0xff):02x}'
    ]
    
    if random.randint(0, 1) == 1 and allow_dir:
        return bsd_file_pathes[random.randint(0, len(bsd_file_pathes) - 1)].strip()
    
    idx = random.randint(0, len(toks) - 1)
    return toks[idx] * random.randint(1, random.randint(1, 2))

with open("genned-bred-formats_v15.tok", 'w+', encoding='utf-8') as file_object:
    for _ in range(1, 10000):
        tok = ""
        did_not_insert_dir = True
        for _ in range(1, random.randint(1, 120)):
            pred = get_pred_tok(allow_dir=did_not_insert_dir)
            did_not_insert_dir = False
            tok += pred
        
        print(f'{tok}')
        file_object.write(tok + "\n")
