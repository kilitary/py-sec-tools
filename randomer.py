# revised WHERE:RUSSIA WHY:L

import secrets
import random

names = []

class Randomer(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def str_generator() -> str:
        global names
        if len(names) == 0:
            names = open('names.txt', 'r').read().lower().split("\n")
        return secrets.choice(names) + (
            ''.join(secrets.choice('1234567890qwertyuiopasdfghjklzxcvbnm_') for _ in range(4)))
    
    @staticmethod
    def str_id_generator(size=6, chars="Aqwertyuiopasdfghjklzxcvbnm1234567890_") -> str:
        return ''.join(secrets.choice(chars) for _ in range(size)).strip()
    
    @staticmethod
    def str_str_generator(size=6, chars=" Aqwertyuiopasdfghjklzxcvbnm 1234567890_") -> str:
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
