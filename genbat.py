import random
import secrets
from enum import Enum, auto
from var_dump import var_dump
from helpers import deb
from outputdebugstring import olog
from randomer import Randomer

pipe = ''
commands = []
code = ''
gotos = []
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

class Assember(object):
	command_pipeline = []
	code = ''
	offset = 0
	ip_offset = 0
	filename = ''

	def __init__(self, filename):
		self.filename = filename

	def __len__(self):
		return len(self.command_pipeline)

	def __getitem__(self, i):
		return self.command_pipeline[i]

	def junk(self, min=0, max=2) -> None:
		for x in range(min, max):
			choose = secrets.choice([1, 2, 3, 4, 5])

			if choose == 1:
				self.push(Command(Operand.ECHO, Randomer.str_id_generator(size=5)))
			elif choose == 2:
				self.push(Command(Operand.TITLE, Randomer.str_id_generator(size=8)))
			elif choose == 3:
				self.push(Command(Operand.REM, Randomer.str_str_generator(size=5)))
			elif choose == 4:
				self.push(Command(Operand.SET, f"{Randomer.rnd_name()}=\"{Randomer.str_str_generator(size=10)}\""))
			elif choose == 5:
				self.push(Command(Operand.SETV, f"{Randomer.rnd_name()}[{random.randint(0, 2500)}]=\"{Randomer.str_str_generator(size=10)}\""))

		return

	def save(self) -> None:
		self.write(self.filename, self.join_code())

	def sort(self) -> None:
		self.command_pipeline = sorted(self.command_pipeline, key=lambda command: command.offset)

	def join_code(self) -> str:
		code = ''

		self.sort()

		#code = '\n'.join(self.command_pipeline)
		for command in self.command_pipeline:
			code += str(command).strip() + f"\n"

		return code.strip()

	def get_operand_at(self, offset):
		operand = [x for x in self.command_pipeline if x.offset == offset]
		return operand[0].operand if len(operand) > 0 else None

	def num_commands(self) -> int:
		return len(self)

	def push(self, command, offset=0) -> int:
		if offset == -1:
			max = self.num_commands() - 1 if self.num_commands() - 1 > 0 else 0
			command.offset = random.randint(0, max)
		# deb(f"push {command} @ {command.offset} ({self.get_operand_at(command.offset)})")
		else:
			command.offset = offset if offset else self.offset

		self.command_pipeline.append(command)
		self.offset += offset

		if ip_debug:
			deb(f'{self.offset:04d} {command} ({len(assember)})')
			var_dump(self.command_pipeline)

		return self.offset

	def write(self, filename: str, code: str) -> None:
		with open(filename, "w") as file:
			file.write("@ECHO ===========================================================\n")
			ret = file.write(code)
			deb(f'\nwritten {ret} bytes to {filename}\r\n')

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

	def __init__(self, operand, param=None, offset=0):
		self.operand = operand
		self.param = param
		self.offset = offset

	def __str__(self):
		param = self.param if self.param is not None else ''
		command = self.operands[self.operand] + " " + param
		return command

if __name__ == '__main__':
	offset = 0
	assember = Assember("mut.cmd")
	max = max_operands = random.randint(11, 21)

	num_gotos = random.randint(5, max)

	ii = ['\\', '|', '/', '-']
	numIi = 0
	ip = 0

	for ng in range(num_gotos):
		assember.junk(min=1, max=13)

	for step in range(0, max_operands - 1):
		if max >= 1611:
			numIi += 1
			if numIi >= len(ii):
				numIi = 0
			currentSym = ii[numIi]
			deb(f'\r[{step / max:.0f}%] mutating code ... {currentSym}', end='')

		# deb(f'offset: {offset}')

		# assember.junk(min=1, max=0)
		# print(f'new ip: {ip}')
		label = Randomer.str_generator()
		ip = assember.push(Command(Operand.GOTO, ":" + label), offset=-1)
		# assember.junk(min=1, max=0)
		# print(f'new ip: {ip}')
		ip = assember.push(Command(Operand.LABEL, ":" + label), offset=-1)

		if step == max - 2:
			assember.push(Command(Operand.EXIT))

	deb(f"{assember.join_code()}")

	assember.save()
