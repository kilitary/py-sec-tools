#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

import random
import logging
from helpers import pgreen, pred, pgray, pblue, pblack, get_computer_uid
from torpy import TorClient
from torpy.utils import *
from torpy.http.requests import do_request
from randomer import Randomer
from urllib import parse
import sys


def get_num_circuit() -> int:
    global prev_num_circuit
    num_circuit = 0
    while num_circuit == prev_num_circuit:
        num_circuit = random.randint(1, 3)
        if num_circuit == prev_num_circuit:
            pred(f'random wants {num_circuit} again')
    prev_num_circuit = num_circuit
    return num_circuit

def request_host_data(stream) -> str:
    payload = 'GET /?ray=' + Randomer.str_id_generator() + \
              f' HTTP/1.1\r\nUser-Agent: natural nature\r\n' + \
              f'Host: {hostname}\r\n\r\n'
    pgreen(f'playload:\n{payload}')
    stream.send(bytes(payload, encoding='utf-8'))
    pblack('receiving ... ', send='')
    recv = recv_exact(stream, 4096)
    buf = str(recv.decode(errors="ignore")[:4096])
    pblack(f'{len(recv)} bytes \r\n\r\n{buf}')
    return buf

pgreen(f'def encoding: {sys.getdefaultencoding()} debug: {__debug__}')

hostname = 'kilitary.ru'  # It's possible use onion hostname here as well
logging.basicConfig(format="%(asctime)s [%(levelname)s] [%(thread)d] %(filename)s(%(funcName)s:%(lineno)d) - %(message)s", level=logging.INFO)
prev_num_circuit = 0

if __name__ == '__main__':
    while True:
        num_circuit = 0
        try:
            with TorClient() as tor:
                pblack('tor client (re)created')
                try:
                    # Choose random guard node and create 3-hops circuit
                    num_circuit = get_num_circuit()
                    assert num_circuit >= 1
                    pblack(f'creating {num_circuit} nodes circuit ... ')

                    with tor.create_circuit(num_circuit) as circuit:
                        pgreen(f'OK')
                        # Create tor stream to host
                        pblack(f'connecting to {hostname} ... ', send='')

                        with circuit.create_stream((hostname, 80)) as stream:
                            pgreen('OK')

                            buf = request_host_data(stream)

                            if "next-experiment" in buf: pgreen('\n\rpye&bye check done\r\n')
                            else: pred('no pay&bye service\r\n')

                            # data = do_request('http://kilitary.ru?zay=' + str(random.randint(0, 99999999)) +
                            #                   parse.quote(f"&push='routers:{num_circuit}/{get_computer_uid()}/{Randomer.str_str_generator()}'"),
                            #                   headers={'User-Agent': 'Mozilla/111.0', 'X-use': 'ddos'}, verbose=1, retries=3)
                            # pblack(f'data {data[0:14096]}')
                except Exception as e:
                    type, value, traceback = sys.exc_info()
                    pred(f'circuit: {e}: {value}:{traceback}')
        except Exception as e:
            type, value, traceback = sys.exc_info()
            pred(f'TorClient: {e}: {value}:{traceback}')
