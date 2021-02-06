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
from enum import Enum, auto
import string
import secrets

pipe = ''
commands = []
code = ''
gotos = []
names = []
ip_offset = 0

class Operand(Enum):
	SET = auto()
	COLOR = auto()
	GOTO = auto()

def write(filename, code):
	with open(filename, "w") as file:
		ret = file.write(code)
		print(f'\r\nwritten {ret} bytes to {filename}\r\n')

def str_id_generator(size=6, chars="qwertyuiopasdfghjklzxcvbnm1234567890"):
	return secrets.choice(names) + "_" + (''.join(secrets.choice(chars) for _ in range(size)))

def pushcmd(cmd, random_offset=False, offset=0) -> int:
	_index = 0
	if offset != 0:
		commands.insert(offset, cmd)
		print(f'offset push: inserting [{cmd}] @ {offset}')
	elif random_offset:
		if len(commands) == 0:
			_index = 0
		else:
			_index = random.randint(0, len(commands) - 1)

		print(f'random push: inserting  [{cmd}] @ {_index}')
		commands.insert(_index, cmd)
		offset = _index
	else:
		commands.append(cmd)
		offset = len(commands)
		print(f'seqntl push: added  [{cmd}] @ {offset}')

	return offset

def pullout():
	global code
	code = commands

def junk(num=1):
	for x in range(0, num):
		choose = random.choice([1, 2, 3])

		if choose == 1:
			offset = pushcmd(f"ECHO {str_id_generator()}", random_offset=True)
		if choose == 2:
			offset = pushcmd(f"TITLE {str_id_generator()}", random_offset=True)
		if choose == 3:
			offset = pushcmd(f"REM {str_id_generator()}", random_offset=True)
	return offset

if __name__ == '__main__':
	max = random.randint(6, 11)
	num_gotos = random.randint(5, max)
	names = open('names.txt', 'r').read().split("\n")

	ii = ['\\', '|', '/', '-', '*']
	numIi = 0
	offset = 0
	for step in range(0, max - 1):
		if (max >= 100000):
			numIi += 1
			if numIi >= len(ii):
				numIi = 0
			currentSym = ii[numIi]
			print(f'\r[{step / max:.0f}%] mutating code ... {currentSym}', end='')

		print(f'offset: {offset}')

		offset = junk(4)

		# offset = pushcmd(f"REM ipoffset {offset} {step}/{max}")

		lab = str_id_generator(size=4)
		offset = pushcmd("GOTO :" + lab, random_offset=True)

		offset = junk(8)

		pushcmd(f":{lab}", offset=offset + 1)

		if step == max - 1:
			pushcmd('EXIT')

	pullout()

	for index, line in enumerate(code):
		print(f'{index:08} {line}')
	print(f"\ncode: {len(commands)} commands")

	write("mut.cmd", "\n".join(code))
