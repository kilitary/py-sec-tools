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
import yara
DIR = "c:\\"
processed = 0

def gather_file_info_win(binary):
	"""
	Borrowed from BDF...
	I could just skip to certLOC... *shrug*
	"""
	flItms = {}
	binary = open(binary, 'rb')
	binary.seek(int('3C', 16))
	flItms['buffer'] = 0
	flItms['JMPtoCodeAddress'] = 0
	flItms['dis_frm_pehdrs_sectble'] = 248
	flItms['pe_header_location'] = struct.unpack('<i', binary.read(4))[0]
	# Start of COFF
	flItms['COFF_Start'] = flItms['pe_header_location'] + 4
	binary.seek(flItms['COFF_Start'])
	flItms['MachineType'] = struct.unpack('<H', binary.read(2))[0]
	binary.seek(flItms['COFF_Start'] + 2, 0)
	flItms['NumberOfSections'] = struct.unpack('<H', binary.read(2))[0]
	flItms['TimeDateStamp'] = struct.unpack('<I', binary.read(4))[0]
	binary.seek(flItms['COFF_Start'] + 16, 0)
	flItms['SizeOfOptionalHeader'] = struct.unpack('<H', binary.read(2))[0]
	flItms['Characteristics'] = struct.unpack('<H', binary.read(2))[0]
	# End of COFF
	flItms['OptionalHeader_start'] = flItms['COFF_Start'] + 20

	# if flItms['SizeOfOptionalHeader']:
	# Begin Standard Fields section of Optional Header
	binary.seek(flItms['OptionalHeader_start'])
	flItms['Magic'] = struct.unpack('<H', binary.read(2))[0]
	flItms['MajorLinkerVersion'] = struct.unpack("!B", binary.read(1))[0]
	flItms['MinorLinkerVersion'] = struct.unpack("!B", binary.read(1))[0]
	flItms['SizeOfCode'] = struct.unpack("<I", binary.read(4))[0]
	flItms['SizeOfInitializedData'] = struct.unpack("<I", binary.read(4))[0]
	flItms['SizeOfUninitializedData'] = struct.unpack("<I",
	                                                  binary.read(4))[0]
	flItms['AddressOfEntryPoint'] = struct.unpack('<I', binary.read(4))[0]
	flItms['PatchLocation'] = flItms['AddressOfEntryPoint']
	flItms['BaseOfCode'] = struct.unpack('<I', binary.read(4))[0]
	if flItms['Magic'] != 0x20B:
		flItms['BaseOfData'] = struct.unpack('<I', binary.read(4))[0]
	# End Standard Fields section of Optional Header
	# Begin Windows-Specific Fields of Optional Header
	if flItms['Magic'] == 0x20B:
		flItms['ImageBase'] = struct.unpack('<Q', binary.read(8))[0]
	else:
		flItms['ImageBase'] = struct.unpack('<I', binary.read(4))[0]
	flItms['SectionAlignment'] = struct.unpack('<I', binary.read(4))[0]
	flItms['FileAlignment'] = struct.unpack('<I', binary.read(4))[0]
	flItms['MajorOperatingSystemVersion'] = struct.unpack('<H',
	                                                      binary.read(2))[0]
	flItms['MinorOperatingSystemVersion'] = struct.unpack('<H',
	                                                      binary.read(2))[0]
	flItms['MajorImageVersion'] = struct.unpack('<H', binary.read(2))[0]
	flItms['MinorImageVersion'] = struct.unpack('<H', binary.read(2))[0]
	flItms['MajorSubsystemVersion'] = struct.unpack('<H', binary.read(2))[0]
	flItms['MinorSubsystemVersion'] = struct.unpack('<H', binary.read(2))[0]
	flItms['Win32VersionValue'] = struct.unpack('<I', binary.read(4))[0]
	flItms['SizeOfImageLoc'] = binary.tell()
	flItms['SizeOfImage'] = struct.unpack('<I', binary.read(4))[0]
	flItms['SizeOfHeaders'] = struct.unpack('<I', binary.read(4))[0]
	flItms['CheckSum'] = struct.unpack('<I', binary.read(4))[0]
	flItms['Subsystem'] = struct.unpack('<H', binary.read(2))[0]
	flItms['DllCharacteristics'] = struct.unpack('<H', binary.read(2))[0]
	if flItms['Magic'] == 0x20B:
		flItms['SizeOfStackReserve'] = struct.unpack('<Q', binary.read(8))[0]
		flItms['SizeOfStackCommit'] = struct.unpack('<Q', binary.read(8))[0]
		flItms['SizeOfHeapReserve'] = struct.unpack('<Q', binary.read(8))[0]
		flItms['SizeOfHeapCommit'] = struct.unpack('<Q', binary.read(8))[0]

	else:
		flItms['SizeOfStackReserve'] = struct.unpack('<I', binary.read(4))[0]
		flItms['SizeOfStackCommit'] = struct.unpack('<I', binary.read(4))[0]
		flItms['SizeOfHeapReserve'] = struct.unpack('<I', binary.read(4))[0]
		flItms['SizeOfHeapCommit'] = struct.unpack('<I', binary.read(4))[0]
	flItms['LoaderFlags'] = struct.unpack('<I', binary.read(4))[0]  # zero
	flItms['NumberofRvaAndSizes'] = struct.unpack('<I', binary.read(4))[0]
	# End Windows-Specific Fields of Optional Header
	# Begin Data Directories of Optional Header
	flItms['ExportTableRVA'] = struct.unpack('<I', binary.read(4))[0]
	flItms['ExportTableSize'] = struct.unpack('<I', binary.read(4))[0]
	flItms['ImportTableLOCInPEOptHdrs'] = binary.tell()
	# ImportTable SIZE|LOC
	flItms['ImportTableRVA'] = struct.unpack('<I', binary.read(4))[0]
	flItms['ImportTableSize'] = struct.unpack('<I', binary.read(4))[0]
	flItms['ResourceTable'] = struct.unpack('<Q', binary.read(8))[0]
	flItms['ExceptionTable'] = struct.unpack('<Q', binary.read(8))[0]
	flItms['CertTableLOC'] = binary.tell()
	flItms['CertLOC'] = struct.unpack("<I", binary.read(4))[0]
	flItms['CertSize'] = struct.unpack("<I", binary.read(4))[0]
	binary.close()
	return flItms

def pred(text):
	print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255, 0, 0, text))
	olog(text)
	flog(text)

def pgray(text):
	print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(11, 110, 0, text))
	flog(text)

def pgreen(text, send='\n'):
	print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(11, 110, 110, text), end=send)
	olog(text)
	flog(text)

def pblue(text):
	print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(111, 210, 110, text))
	flog(text)

def pblack(text):
	print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(21, 25, 244, text))
	flog(text)
	olog(text)

def list_files_recursive(path):
	"""
	Function that receives as a parameter a directory path
	:return list_: File List and Its Absolute Paths
	"""
	import os

	current_files = []
	total_files = 0
	# r = root, d = directories, f = files
	pgreen(f"traveling {path} ...", send='')
	st_time = time.time()
	for r, d, f in os.walk(path):
		for current_file in f:
			total_files += 1
			if ".exe" in current_file or ".dll" in current_file or "-crypted" in current_file or ".sys" in current_file:
				current_files.append(os.path.join(r, current_file))
				if time.time() - st_time >= 0.3:
					st_time = time.time()
					pgreen(f"\rtraveling {len(current_files)} / {total_files} [{r}] ... ", send='')

	lst = [internal_file for internal_file in current_files]
	return lst

def suitable(name):
	goods = ['exe', 'sys', 'dll']
	name = name.lower()
	for good in goods:
		if 'winsxs' in name or "rollup" in name or "dotnet" in name:
			return False
		if name.endswith(good):
			return True
	return False

def mycallback(data):
	print(data)
	return yara.CALLBACK_CONTINUE

# Press the red button
if __name__ == '__main__':
	# yara.set_config(stack_size=4 * 1024 * 1024)
	# yara.set_config(max_strings_per_rule=50000, stack_size=4 * 1024 * 1024)
	# yara.set_config(max_match_data=1024)

	pblack(f'[{os.getcwd()}] loading rules ...')
	rules = []
	try:
		rules = yara.compile('petarget.rules', error_on_warning=False)
	except Exception as e:
		pred(f'{e}')
		# exc_type, exc_value, exc_traceback = sys.exc_info()
		# pred(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
		sys.exit(-1)

	for rule in rules:
		if rule.is_private != True:
			pblack(f'rule {rule.identifier}: ' + rule.meta.get("description", "<none>") + " (private=" + str(rule.is_private) + ")" + " (global=" + str(rule.is_global) + ")")

	pblack(f'collecting files from {DIR}...')
	current_year = int(time.localtime().tm_year)
	files = list_files_recursive(DIR)
	ii = ['\\', '|', '/', '-', '*']
	numIi = 0
	pblack(f'scanning {len(files)} files ...')
	st_time = time.time()
	for file in files:
		try:
			interesting_file = False
			numIi += 1
			if numIi >= len(ii):
				numIi = 0
			currentSym = ii[numIi]

			if time.time() - st_time >= 0.3:
				st_time = time.time()
				pgreen(f"\rScanning {currentSym} [{file}]", send='')

			if not suitable(file):
				continue

			matches = rules.match(file)
			if len(matches):
				interesting_file = True

			if not interesting_file:
				continue

			pblack(f"\r=> [{file}]" + ('=' * 50))

			m = magic.Magic(keep_going=True, uncompress=True)
			pgray(f'type: {m.from_file(file)}')

			for match in matches:
				pred(f'sign <{match}>')

			try:
				pe = pefile.PE(file, fast_load=True)
			except Exception as err:
				pred(f"\nPE: {err}")
				continue
			#
			if hex(pe.OPTIONAL_HEADER.Magic) == '0x10b':
				pgray("32-bit binary")
			elif hex(pe.OPTIONAL_HEADER.Magic) == '0x20b':
				pgray("64-bit binary")
			#
			pgray("Magic : " + hex(pe.OPTIONAL_HEADER.Magic) + " " + "Machine: " + hex(pe.FILE_HEADER.Machine) +
			       " TimeDateStamp : " + pe.FILE_HEADER.dump_dict()['TimeDateStamp']['Value'].split('[')[1][:-1])

			# pe_data = gather_file_info_win(file)
			# timestamp = datetime.fromtimestamp(pe_data['TimeDateStamp'])
			# pgray(f'alternate time: {timestamp.strftime("%Y-%m-%d %H:%M:%S")}')

			# pblack("NumberOfSections : " + hex(pe.FILE_HEADER.NumberOfSections) + " (" + str(pe.FILE_HEADER.NumberOfSections) + ") " +
			#        "Characteristics flags : " + hex(pe.FILE_HEADER.Characteristics))
			# pblack("ImageBase : " + hex(pe.OPTIONAL_HEADER.ImageBase) +
			#        " SizeOfImage : " + hex(pe.OPTIONAL_HEADER.SizeOfImage) + " (" + str(pe.OPTIONAL_HEADER.SizeOfImage) + ")")
			# pblack("FileAlignment : " + hex(pe.OPTIONAL_HEADER.FileAlignment) + " (" + str(pe.OPTIONAL_HEADER.FileAlignment) + ")" +
			#        " SectionAlignment : " + hex(pe.OPTIONAL_HEADER.SectionAlignment) + " (" + str(pe.OPTIONAL_HEADER.SectionAlignment) + ")")
			# pblack("DllCharacteristics flags : " + hex(pe.OPTIONAL_HEADER.DllCharacteristics) +
			#        " Image subsystem: " + hex(pe.OPTIONAL_HEADER.Subsystem))
			#
			# for entry in pe.OPTIONAL_HEADER.DATA_DIRECTORY:
			# 	if entry.Size > 0:
			# 		pgray(entry.name + " " + str(entry.Size) + "b @ " + hex(entry.VirtualAddress))
			# 	else:
			# 		pblue(entry.name + " <empty>")
			#
			# for section in pe.sections:
			# 	pblack(section.Name.decode().rstrip('\x00').ljust(11) + str("V " + str(section.Misc_VirtualSize)).rjust(11) +
			# 	       str(" R " + str(section.SizeOfRawData)).rjust(11) + " @ " + hex(section.VirtualAddress).ljust(11))

			processed += 1

		except Exception as err:
			pred(f"Exception: {err}: {sys.exc_info()[1]}")

	pblack(f"processed {processed} files")
