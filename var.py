from iced_x86 import *

buffer = b'\x90\x31\xc9\x31\xca\x31\xcb'
EXAMPLE_CODE_BITNESS = 64
EXAMPLE_CODE_RIP = 0x0000_7FFA_C46A_CDA4
buffer2 = \
	b"\x48\x89\x5C\x24\x10\x48\x89\x74\x24\x18\x55\x57\x41\x56\x48\x8D" \
	b"\xAC\x24\x00\xFF\xFF\xFF\x48\x81\xEC\x00\x02\x00\x00\x48\x8B\x05" \
	b"\x18\x57\x0A\x00\x48\x33\xC4\x48\x89\x85\xF0\x00\x00\x00\x4C\x8B" \
	b"\x05\x2F\x24\x0A\x00\x48\x8D\x05\x78\x7C\x04\x00\x33\xFF"

# Create the decoder and initialize RIP
decoder = Decoder(EXAMPLE_CODE_BITNESS, buffer2)
formatter = Formatter(FormatterSyntax.MASM)
for instr in decoder:
	disasm = formatter.format(instr)
	# You can also get only the mnemonic string, or only one or more of the operands:
	#   mnemonic_str = formatter.format_mnemonic(instr, FormatMnemonicOptions.NO_PREFIXES)
	#   op0_str = formatter.format_operand(instr, 0)
	#   operands_str = formatter.format_all_operands(instr)

	start_index = instr.ip - EXAMPLE_CODE_RIP
	bytes_str = buffer[start_index:start_index + instr.len].hex().upper()
	# Eg. "00007FFAC46ACDB2 488DAC2400FFFFFF     lea       rbp,[rsp-100h]"
	print(f"{instr.ip:016X} {bytes_str:20} {disasm}")
