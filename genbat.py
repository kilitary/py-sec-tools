import time
import subprocess
import os
import pefile
import sys
from pprint import pprint
import glob
import time
import io
from datetime import datetime
import struct
import shutil
from helpers import flog
from optparse import OptionParser
from ctypes import *
from inspect import getmembers
from var_dump import var_dump
import filetype
from outputdebugstring import olog
import sys, traceback
import magic
import random
from enum import Enum

pipe = ''
cmds = []
code = ''
gotos = []

def write(filename, code):
    with open(filename, "w") as file:
        ret = file.write(code)
        print(f'\r\n=> written {ret} bytes to {filename}\r\n')

def str_id_generator(size=6, chars="qwertyuiopasdfghjklzxcvbnm1234567890"):
    return (''.join(random.choice(chars) for _ in range(size)))

def pushcmd(cmd, random_offset=False):
    if random_offset:
        if len(cmds) == 0:
            idx = 0
        else:
            idx = random.randint(0, len(cmds) - 1)
        cmds.insert(idx, cmd)
    else:
        cmds.append(cmd)

def pullout():
    global code
    code = '\n'.join(cmds)

if __name__ == '__main__':
    num_gotos = random.randint(1, 22)

    for x in range(0, num_gotos):
        lab = 'g' + str_id_generator()
        gotos.append(f"{lab}")
        pushcmd(f":{lab}", random_offset=True)

    for x in range(0, random.randint(3, 8)):
        label = gotos[random.randint(0, len(gotos) - 1)]
        pushcmd("goto :" + label, random_offset=True)
        pushcmd(f"echo {str_id_generator()}", random_offset=False)

    pullout()
    print(f"=> code ({len(cmds)} commands):\r\n\r\n{code}")

    write("mut.cmd", code)
