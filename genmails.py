import argparse
import random
import json
import string
from var_dump import var_dump

def str_id_generator(size=6, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars).lower() for _ in range(size))

def deb(*arguments, **keywords):
    for kw in keywords:
        print(f"-> {kw}: {keywords[kw]}")

def add_email(email):
    with open(args.outfile, "at") as of:
        of.write(email + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gen emails')
    parser.add_argument('names', type=str, help='names/words')
    parser.add_argument('outfile', type=str, help='Output file (with emails)')
    parser.add_argument('num', type=int, help='num of emails')
    
    args = parser.parse_args()
    
    with open(args.names, "rt") as inp:
        names = inp.readlines()
    
    random.shuffle(names)
    
    for num_email in range(0, args.num):
        rnd_index = random.randint(0, len(names) - 1)
        
        flname = str(names[rnd_index:rnd_index + 1][0]).strip()
        prefix = ''
        
        if random.choice([True, False]):
            prefix = f"{str_id_generator(size=random.randint(0, 4))}"
        
        postfix = ''
        
        if random.choice([True, False]):
            postfix = f"{str_id_generator(size=random.randint(0, 4))}"
        
        email = str(prefix + f'{flname}' + postfix + "@gmail.com").lower().strip()
        print(email)
        add_email(email)
# deb(email=f"=> {email}", prefix=prefix, postfix=postfix)
