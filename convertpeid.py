import os, sys
import requests
from var_dump import var_dump
import re
import random

def str_id_generator(size=6, chars='qwertyuiopasdfghjklzxcvbnm'):
	return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
	data = requests.get('https://raw.githubusercontent.com/wolfram77web/app-peid/master/userdb.txt').text
	# print(f'{data}')
	matches = re.findall(r"\[([^\]]*?)\].+?signature\s+?=(.*?)ep_only", data, flags=re.RegexFlag.S | re.RegexFlag.M)
	# var_dump(str(lines))

	# var_dump(matches)
	# print(f'{matches.group(1)}')
	with open('peid.rules', 'w') as file:
		for match in matches:
			sign = initial_sign = match[1].strip().replace(' ', '')
			if re.search(r'[^A-F0-9\?]', initial_sign):
				print(f'skip bad sign [{initial_sign}]')
				continue

			sign_length = len(initial_sign)
			desc = re.sub('[^A-Za-z0-9 ]', '_', str(match[0]).strip('\n\r\t/').replace('/', ''))
			id = re.sub('[^a-z0-9A-Z]', '_', desc).replace('__', '_') + '_' + str_id_generator(size=6)
			sign = '{' + re.sub(r'[^A-F0-9 \?]', '', sign).replace('  ', '') + '}'
			bad = sign_length % 2

			print(f'{id}: {desc} {len(sign) / 2:.0f} bytes [{bad}] from [{initial_sign}]')

			if bad:
				print(f'bad sign')
				continue

			try:
				file.write(f'rule {id}\n'
				           '{\r\n'
				           '\tmeta:\n'
				           f'\t\tdescription = "{desc}"\r\n'
				           '\tstrings:\n'
				           f'\t\t$a = {sign}\r\n'
				           '\tcondition:\n'
				           '\t\tall of them\r\n'
				           '}' + '\r\n')
			except Exception as e:
				print(f'write error: {e}')
