import random
import secrets
from enum import Enum, auto
from var_dump import var_dump
from helpers import deb
from outputdebugstring import olog
from randomer import Randomer

pipe = ''
commands = []
_code = ''
gotos = []
ip_debug = False
ii = ['\\', '|', '/', '-']

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
	_command_pipeline = []
	_code = None
	_offset = 0
	ip_offset = 0
	filename = ''

	def __init__(self, filename):
		self.filename = filename

	def __len__(self):
		return len(self._command_pipeline)

	def __getitem__(self, i):
		return self._command_pipeline[i]

	def junk(self, min=0, max=2) -> None:
		for x in range(min, max):
			choose = secrets.choice([1, 2, 3, 4, 5])

			if choose == 1:
				self.push_command(Command(Operand.ECHO, Randomer.str_id_generator(size=random.randint(0, 250))))
			elif choose == 2:
				self.push_command(Command(Operand.TITLE, Randomer.str_id_generator(size=random.randint(0, 200))))
			elif choose == 3:
				self.push_command(Command(Operand.REM, Randomer.str_str_generator(size=random.randint(0, 250))))
			elif choose == 4:
				self.push_command(Command(Operand.SET, f"{Randomer.rnd_name()}=\"{Randomer.str_str_generator(size=random.randint(0, 250))}\""))
			elif choose == 5:
				self.push_command(Command(Operand.SETV, f"{Randomer.rnd_name()}[{random.randint(0, 250)}]=\"{Randomer.str_str_generator(size=random.randint(0, 250))}\""))

		return

	def save(self) -> None:
		# var_dump(self._command_pipeline)
		self.write(self.filename, self.get_code())

	def sort(self) -> None:
		self._command_pipeline = sorted(self._command_pipeline, key=lambda command: command.offset)

	def get_code(self) -> str:
		if self._code is None:
			deb(f'\r\nsorting code according to offset order ...')
			self.sort()

			step = 0
			code = ''
			num = len(self._command_pipeline)
			numIi = 0

			for command in self._command_pipeline:
				code += str(command).strip() + f"\n"
				step += 1

				numIi += 1
				if numIi >= len(ii):
					numIi = 0
				currentSym = ii[numIi]

				deb(f'\rjoining code ... {step / num * 100.0:.1f}% (line {step} of {num}, {len(code)} bytes) {currentSym}', end='')

			self._code = code.strip()
		return self._code

	def get_operand_at(self, offset):
		rec = [x for x in self._command_pipeline if x.offset == offset]
		return rec[0].operand if len(rec) > 0 else None

	def num_commands(self) -> int:
		return len(self)

	def push_command(self, command, offset=0) -> int:
		if offset == -1:
			max = self.num_commands() - 1 if self.num_commands() - 1 > 0 else 0
			command.offset = random.randint(0, max)
		# deb(f"push {command} @ {command.offset} ({self.get_operand_at(command.offset)})")
		else:
			command.offset = offset if offset else self._offset + 1

		self._command_pipeline.append(command)
		self._offset = command.offset

		if ip_debug:
			deb(f'{self._offset:04d} {command} ({len(assember)})')
			var_dump(self._command_pipeline)

		return self._offset

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
	max = max_operands = random.randint(111, 111111)

	num_gotos = random.randint(1, max)

	numIi = 0
	ip = 0

	# for ng in range(num_gotos):
	#	assember.junk(min=1, max=4)

	for step in range(0, max_operands - 1):
		if max >= 111:
			numIi += 1
			if numIi >= len(ii):
				numIi = 0
			currentSym = ii[numIi]
			deb(f'\r[{step / max * 100.0:.0f}%] generating code ... {currentSym}', end='')

		# deb(f'offset: {offset}')

		assember.junk(min=11, max=34)
		label = Randomer.str_generator()
		ip = assember.push_command(Command(Operand.GOTO, ":" + label), offset=-1)
		assember.junk(min=11, max=34)
		ip = assember.push_command(Command(Operand.LABEL, ":" + label))

		if step == max - 2:
			assember.push_command(Command(Operand.EXIT))

	deb(f"{assember.get_code()}")

	assember.save()
