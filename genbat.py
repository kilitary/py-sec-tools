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

ip_debug = False

class Operand(Enum):
	SET = auto()
	SETV = auto()
	COLOR = auto()
	GOTO = auto()
	TITLE = auto()
	ECHO = auto()
	REM = auto()

class Command(object):
	operands = {
		Operand.REM  : "REM",
		Operand.ECHO : "ECHO",
		Operand.TITLE: "TITLE",
		Operand.SET  : "SET",
		Operand.SETV : "SET",
		Operand.COLOR: "COLOR",
		Operand.GOTO : "GOTO"
	}

	def __init__(self, operand, param):
		self.operand = operand
		self.param = param
		self.offset = 0

	def __str__(self):
		command = operands[self.operand] + " " + self.param
		return command

def write(filename, code):
	with open(filename, "w") as file:
		file.write("@ECHO ===========================================================\n")
		ret = file.write(code)
		print(f'\r\nwritten {ret} bytes to {filename}\r\n')

def str_lbl_generator(size=6, chars="qwertyuiopasdfghjklzxcvbnm1234567890"):
	return secrets.choice(names)  # + "_" + (''.join(secrets.choice(chars) for _ in range(size)))

def str_id_generator(size=6, chars="Aqwertyuiopasdfghjklzxcvbnm1234567890"):
	return ''.join(secrets.choice(chars) for _ in range(size))

def str_str_generator(size=6, chars=" Aqwertyuiopasdfghjklzxcvbnm 1234567890 "):
	y = ''
	for x in range(0, random.randint(1, 4)):
		y += ''.join(secrets.choice(chars) for _ in range(size))
	return y

def pushcmd(cmd, random_offset=False, offset=0) -> int:
	_index = 0
	if offset != 0:
		commands.insert(offset, cmd)
		if ip_debug:
			print(f'offset push: inserting [{cmd}] @ {offset} ({len(commands)} total)')
	elif random_offset:
		if len(commands) == 0:
			_index = 0
		else:
			_index = random.randint(0, len(commands) - 1)
		if ip_debug:
			print(f'random push: inserting  [{cmd}] @ {_index} ({len(commands)} total)')
		commands.insert(_index, cmd)
		offset = _index
	else:
		commands.append(cmd)
		offset = len(commands)
		if ip_debug:
			print(f'seqntl push: added  [{cmd}] @ {offset} ({len(commands)} total)')

	return offset

def pullout():
	global code
	code = commands

def junk(num=1):
	offset = 0

	for x in range(num):
		choose = secrets.choice([1, 2, 3, 4, 5])

		if choose == 1:
			offset = pushcmd(f"ECHO {str_id_generator(size=5)}")
		if choose == 2:
			offset = pushcmd(f"TITLE {str_id_generator(size=11)}")
		if choose == 3:
			offset = pushcmd(f"REM {str_str_generator(size=10)}")
		if choose == 4:
			offset = pushcmd(f"SET {secrets.choice(names)}=\"{str_str_generator(size=10)}\"")
		if choose == 5:
			offset = pushcmd(f"SET {secrets.choice(names)}[{random.randint(0, 500)}]=\"{str_str_generator(size=10)}\"")

	return offset

if __name__ == '__main__':
	# max = random.randint(6, 33)
	max = max_operands = random.randint(5, 11)
	print(f'prefill ({max})...')
	for x in range(0, max):
		pushcmd(f'REM {str_str_generator(size=8)}')

	num_gotos = random.randint(5, max)
	names = open('names.txt', 'r').read().split("\n")

	ii = ['\\', '|', '/', '-']
	numIi = 0
	offset = 0
	for step in range(0, max_operands - 1):
		if max >= 100000:
			numIi += 1
			if numIi >= len(ii):
				numIi = 0
			currentSym = ii[numIi]
			print(f'\r[{step / max:.0f}%] mutating code ... {currentSym}', end='')

		# print(f'offset: {offset}')

		offset = junk(2)

		lab = str_lbl_generator(size=4)
		pushcmd("GOTO :" + lab, random_offset=True)

		offset = junk(2)

		pushcmd(f":{lab}", offset=offset + 1)

		if step == max - 2:
			pushcmd('EXIT')

	pullout()

	for index, line in enumerate(code):
		print(f'{index:08} {line}')

	print(f"\ncode: {len(commands)} commands")

	write("mut.cmd", "\n".join(code))
