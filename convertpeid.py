import os, sys
import requests
from var_dump import var_dump
import re
import random
from outputdebugstring import olog

def str_id_generator(size=6, chars='qwertyuiopasdfghjklzxcvbnm'):
    return ''.join(random.choice(chars) for _ in range(size))

def dir_files(path):
    """
	Function that receives as a parameter a directory path
	:return list_: File List and Its Absolute Paths
	"""
    global virtualization_detected
    current_files = []
    total_files = 0
    import time
    
    st_time = time.time()
    for dirpath, dirnames, filenames in os.walk(path):
        for current_file in filenames:
            full = os.path.join(dirpath, current_file)
            current_files.append(full)
    
    lst = [internal_file for internal_file in current_files]
    return lst

def empty_dest_dir():
    delete_files = dir_files("peid_rules")
    if len(delete_files) > 0:
        print(f'deleting {len(delete_files)} files')
        for file in delete_files:
            os.unlink(file)

if __name__ == '__main__':
    empty_dest_dir()
    data = requests.get('https://raw.githubusercontent.com/wolfram77web/app-peid/master/userdb.txt').text
    # print(f'{data}')
    matches = re.findall(r"\[([^\]]*?)\].+?signature\s+?=(.*?)ep_only", data, flags=re.RegexFlag.S | re.RegexFlag.M)
    # var_dump(str(lines))
    
    # var_dump(matches)
    # print(f'{matches.group(1)}')
    
    os.unlink('peid.rules')
    signs = {}
    with open('peid.rules', 'w') as include_file:
        for match in matches:
            sign = initial_sign = match[1].strip().replace(' ', '')
            if re.search(r'[^A-F0-9\?]', initial_sign):
                print(f'skip bad sign [{initial_sign}]')
                continue
            
            sign_length = len(initial_sign)
            desc = re.sub('[^A-Za-z0-9 ]', '_', str(match[0]).strip('\n\r\t/').replace('/', ''))
            id = re.sub('[^a-z0-9A-Z]', '_', desc).replace('__', '_') + '_' + str_id_generator(size=6)
            id_clean = re.sub('[^a-z0-9A-Z]', '_', desc)
            if signs.get(id_clean, None) is None:
                signs[id_clean] = 0
            signs[id_clean] += 1
            sign = '{' + re.sub(r'[^A-F0-9 \?]', '', sign).replace('  ', '') + '}'
            bad = sign_length % 2
            
            print(f'{id}: {desc} {len(sign) / 2:.0f} bytes [{bad}] from [{initial_sign}]')
            
            if bad:
                print(f'bad sign')
                continue
            
            filename = id + '_x' + repr(signs[id_clean])
            olog(f'id: {filename}')
            try:
                include_file.write(f'include "peid_rules/{filename}.rule"' + "\n")
            except Exception as e:
                print(f'write error: {e}')
            
            with open(f'peid_rules/{filename}.rule', 'w') as file:
                file.write(f'rule _{id}\n'
                           '{\r\n'
                           '\tmeta:\n'
                           f'\t\tdescription = "{desc}"\r\n'
                           '\tstrings:\n'
                           f'\t\t$a = {sign}\r\n'
                           '\tcondition:\n'
                           '\t\t$a in (entrypoint..entrypoint + 11111110)\r\n'
                           '}' + '\r\n')
