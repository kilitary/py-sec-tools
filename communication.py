#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com

import random
import logging
from torpy.http.requests import do_request as http

from crawler_config import Config
from helpers import get_computer_uid


def log(msg: str):
    ret = ''
    tryes = 0
    while ret != 'ok' and tryes < 5:
        try:
            ret = http('http://' + Config.COORDINATION_SERVER + '/log.php',
                       data={"msg": msg},
                       method='post', hops=3, verbose=0, retries=6)
            print(f'ret: {ret}')
        except Exception as e:
            print(f'http: {e}')
        tryes += 1
    return ret

class Server(object):
    
    def __init__(self, tor=None, circuit=None):
        pass

logging.basicConfig(format="%(asctime)s [%(levelname)s] [%(thread)d] %(filename)s(%(funcName)s:%(lineno)d) - %(message)s", level=logging.ERROR)
logger = logging.getLogger(__name__)
s = Server()
logger.info(f'{get_computer_uid()} works!, {random.randbytes(11128).hex()}')
