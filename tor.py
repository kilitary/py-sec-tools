#  ./Copyright 2022 Sergey Efimov (kilitary and deconf) kilitary@gmail.com

import random
import logging
from helpers import pgreen, pred, pgray, pblue, pblack, get_computer_uid
from torpy import TorClient
from torpy.utils import recv_all
from torpy.http.requests import do_request
from randomer import Randomer
from urllib import parse
import sys


pgreen(f'def encoding: {sys.getdefaultencoding()}')

hostname = 'kilitary.ru'  # It's possible use onion hostname here as well
logging.basicConfig(format="%(asctime)s [%(levelname)s] [%(thread)d] %(filename)s(%(funcName)s:%(lineno)d) - %(message)s", level=logging.INFO)

if __name__ == '__main__':
    while True:
        prev_num_circuit = num_circuit = 0
        try:
            with TorClient() as tor:
                pblack('tor client (re)created')
                try:
                    # Choose random guard node and create 3-hops circuit
                    while num_circuit == prev_num_circuit:
                        num_circuit = random.randint(2, 6)
                        if num_circuit == prev_num_circuit:
                            pred(f'random wants {num_circuit} again')
                    prev_num_circuit = num_circuit
                    
                    pblack(f'creating {num_circuit} nodes circuit ... ')
                    with tor.create_circuit(num_circuit) as circuit:
                        pgreen(f'OK')
                        # Create tor stream to host
                        pblack(f'connecting to {hostname} ... ', send='')
                        with circuit.create_stream((hostname, 25)) as stream:
                            pgreen('OK')
                            payload = 'GET /?ray=' + Randomer.str_id_generator() + f' HTTP/1.1\r\nUser-Agent: natural nature\r\n' \
                                                                                   ' Connection: close\r\nHost: {hostname}\r\n\r\n'
                            pgreen(f'playload:\n{payload}')
                            stream.send(bytes(payload, encoding='utf-8'))
                            pblack('receiving ... ', send='')
                            recv = recv_all(stream)
                            buf = str(recv.decode(errors="ignore")[:4096])
                            pblack(f'{len(recv)} bytes \r\n\r\n{buf}')
                            if buf.count("bye=ok"):
                                pgreen('\n\rpye&bye check done\r\n')
                            else:
                                pred('no pay&bye service\r\n')
                            data = do_request('http://kilitary.ru?zay=' + str(random.randint(0, 99999999)) + parse.quote(f"&push='routers:{num_circuit}/{get_computer_uid()}/{Randomer.str_str_generator()}'"),
                                              headers={'User-Agent': 'Mozilla/111.0', 'X-use': 'ddos'}, verbose=1, retries=3)
                            pblack(f'data {data[0:14096]}')
                except Exception as e:
                    pred(f"circuit: {e}")
        except Exception as e:
            type, value, traceback = sys.exc_info()
            pred(f'TorClient: {e}: {value}:{traceback}')
