
#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com

import os
import random
import re
import shutil
import string
import sys
import time
from os import getenv
from struct import *
import platform
import logging
import binascii
import threading
import io
import subprocess
import locale
import atexit
from elasticsearch import Elasticsearch
from var_dump import var_dump
import secrets
import random
import re
import base64
from pprint import pprint, pformat
import redis
import atexit
from datetime import datetime
import traceback
import socket

class Randomer(object):
	def __init__(self):
		pass

	@staticmethod
	def str_generator() -> str:
		global names
		if len(names) == 0:
			names = open('names.txt', 'r').read().lower().split("\n")
		return secrets.choice(names) + "_" + (''.join(secrets.choice('1234567890') for _ in range(4)))

	@staticmethod
	def str_id_generator(size=6, chars="Aqwertyuiopasdfghjklzxcvbnm1234567890") -> str:
		return ''.join(secrets.choice(chars) for _ in range(size)).strip()

	@staticmethod
	def str_str_generator(size=6, chars=" Aqwertyuiopasdfghjklzxcvbnm 1234567890 ") -> str:
		y = ''
		for x in range(0, random.randint(1, 4)):
			y += ''.join(secrets.choice(chars) for _ in range(size)).strip()
		return y.strip()

	@staticmethod
	def rnd_name() -> str:
		global names
		if len(names) == 0:
			names = open('names.txt', 'r').read().lower().split("\n")
		return secrets.choice(names)

if __name__ == '__main__':
	HOST = 'kilitary.ru'
	PORT = 25
	tot_bytes = 0

	# HOST = '173.194.73.27'

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print(f'connecting ...')
		s.connect((HOST, PORT))
		s.sendall(b'EHLO anal\r\n')

		data = s.recv(1024)
		print(f'{data.decode("utf8").strip()}')
		s.sendall(b'MAIL FROM:<comm@gmail.com> SIZE=1\r\n')
		data = s.recv(1024)
		print(f'{data.decode("utf8").strip()}')
		s.sendall(b'RCPT TO: <kilitary@gmail.com>\r\n')
		data = s.recv(1024)
		print(f'{data.decode("utf8").strip()}')
		s.sendall(b'DATA\r\n')
		data = s.recv(1024)
		print(f'{data.decode("utf8").strip()}')
		s.setblocking(True)
		log_time = sec_bytes = 0

		while True:
			content = b'\r\n' + (b'A' * secrets.choice(range(1, 15))) + str.encode(Randomer.str_str_generator(size=44)) + b"\r\n"
			try:
				sent = s.send(content)
			except Exception as e:
				print(f'exp: {e}')
				exit(0)

			tot_bytes += sent

			if time.time() - log_time >= 1:
				print(f'\r{tot_bytes} ({tot_bytes / 1024.0 / 1024.0:.1f}MB) sent={sent} speed={sec_bytes / 1024.0 / 1024.0:.1f}MB/s', end='')
				sec_bytes = 0
				log_time = time.time()
			else:
				sec_bytes += sent
