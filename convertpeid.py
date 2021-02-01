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
			initial_sign = str(match[1]).strip().replace(' ', '')
			sign_length = len(initial_sign)
			sign = str(match[1]).strip().replace('/', '').replace(' ', '')
			desc = str(match[0]).strip('\n\r\t/').replace('/', '')
			id = re.sub('[^a-z0-9A-Z]', '_', desc).replace('__', '_') + str(random.randint(101111,2211111))
			sign = '{' + re.sub('[^A-F0-9 \?]', '', sign).replace('  ', '') + '}'
			print(f'{id}: {desc} {len(sign) / 2:.0f} bytes [{sign_length%2}] from [{initial_sign}]]')

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
