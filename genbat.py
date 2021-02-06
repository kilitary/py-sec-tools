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
from helpers import flog, deb

pipe = ''
commands = []
code = ''
gotos = []
names = []
ip_offset = 0
ip_debug = False

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

class Reassember(object):
	command_pipeline = []
	code = ''
	offset = 0

	def __init__(self, filename):
		self.filename = filename

	def __len__(self):
		return len(self.command_pipeline)

	def save(self) -> None:
		self.write(self.filename, self.assemble_code())

	def assemble_code(self) -> str:
		code = ''
		pipeline = sorted(self.command_pipeline, key=lambda command: command.offset)

		for command in pipeline:
			code += str(command).strip() + f"\n"
		return code.strip()

	def push_command(self, command) -> int:
		command.offset = self.offset
		self.command_pipeline.append(command)
		self.offset += 1

		if ip_debug:
			deb(f'{self.offset:08d} {command} ({len(reassember)})')

		return self.offset

	def write(self, filename: str, code: str) -> None:
		with open(filename, "w") as file:
			file.write("@ECHO ===========================================================\n")
			ret = file.write(code)
			deb(f'\r\nwritten {ret} bytes to {filename}\r\n')

class Command(object):
	operands = {
		Operand.LABEL: "",
		Operand.EXIT : "EXIT",
		Operand.REM  : "REM",
		Operand.ECHO : "ECHO",
		Operand.TITLE: "TITLE",
		Operand.SET  : "SET",
		Operand.SETV : "SET",
		Operand.COLOR: "COLOR",
		Operand.GOTO : "GOTO"
	}

	def __init__(self, operand, param=None):
		self.operand = operand
		self.param = param
		self.offset = 0

	def __str__(self):
		param = self.param if self.param is not None else ''
		command = self.operands[self.operand] + " " + param
		return command

def str_lbl_generator() -> str:
	return secrets.choice(names)  # + "_" + (''.join(secrets.choice(chars) for _ in range(size)))

def str_id_generator(size=6, chars="Aqwertyuiopasdfghjklzxcvbnm1234567890") -> str:
	return ''.join(secrets.choice(chars) for _ in range(size)).strip()

def str_str_generator(size=6, chars=" Aqwertyuiopasdfghjklzxcvbnm 1234567890 ") -> str:
	y = ''
	for x in range(0, random.randint(1, 4)):
		y += ''.join(secrets.choice(chars) for _ in range(size)).strip()
	return y.strip()

def junk(min=0, max=2) -> None:
	for x in range(min, max):
		choose = secrets.choice([1, 2, 3, 4, 5])

		if choose == 1:
			reassember.push_command(Command(Operand.ECHO, str_id_generator(size=5)))
		elif choose == 2:
			reassember.push_command(Command(Operand.TITLE, str_id_generator(size=8)))
		elif choose == 3:
			reassember.push_command(Command(Operand.REM, str_str_generator(size=5)))
		elif choose == 4:
			reassember.push_command(Command(Operand.SET, f"{secrets.choice(names)}=\"{str_str_generator(size=10)}\""))
		elif choose == 5:
			reassember.push_command(Command(Operand.SETV, f"{secrets.choice(names)}[{random.randint(0, 500)}]=\"{str_str_generator(size=10)}\""))

	return

if __name__ == '__main__':
	offset = 0
	reassember = Reassember("mut.cmd")
	max = max_operands = random.randint(5, 11)

	num_gotos = random.randint(5, max)
	names = open('names.txt', 'r').read().split("\n")

	ii = ['\\', '|', '/', '-']
	numIi = 0

	for step in range(0, max_operands - 1):
		if max >= 100000:
			numIi += 1
			if numIi >= len(ii):
				numIi = 0
			currentSym = ii[numIi]
			deb(f'\r[{step / max:.0f}%] mutating code ... {currentSym}', end='')

		# deb(f'offset: {offset}')

		junk(min=1, max=2)
		lab = str_lbl_generator()
		reassember.push_command(Command(Operand.GOTO, ":" + lab))

		junk(min=1, max=2)
		reassember.push_command(Command(Operand.LABEL, ":" + lab))

		if step == max - 2:
			reassember.push_command(Command(Operand.EXIT))

	deb(f"{reassember.assemble_code()}")

	reassember.save()
