import random
import logging

from torpy import TorClient
from torpy.utils import recv_all
from torpy.http.requests import do_request

hostname = 'kb5eceekyonjsv5p.onion'  # It's possible use onion hostname here as well
logging.basicConfig(format="%(asctime)s [%(levelname)s] [%(thread)d] %(filename)s(%(funcName)s:%(lineno)d) - %(message)s", level=logging.WARNING)

if __name__ == '__main__':
	while True:
		try:
			with TorClient() as tor:
				print('tor client (re)created')
				try:
					# Choose random guard node and create 3-hops circuit
					num_circuit = random.randint(2, 6)
					print(f'creating {num_circuit} nodes circuit ... ', end='')
					with tor.create_circuit(num_circuit) as circuit:
						print(f'OK')
						# Create tor stream to host
						print(f'connecting to {hostname} ... ', end='')
						with circuit.create_stream((hostname, 80)) as stream:
							print('OK')
							# Now we can communicate with host
							stream.send(b'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % hostname.encode())
							print('receiving ... ', end='')
							recv = recv_all(stream)
							print(f'{len(recv)} bytes \r\n\r\n{recv.decode()[:4096]}')
					data = do_request('https://httpbin.org/headers', headers={'User-Agent': 'Mozilla/5.0', 'X-re-use': 'ddos'}, verbose=1, retries=3)
					print(f'data {data}')
					data = do_request('https://kilitary.ru?pay=1', headers={'User-Agent': 'Mozilla/5.0', 'X-use': 'ddos'}, verbose=1, retries=3)
					print(f'data {data[0:4096]}')
				except Exception as e:
					print(f"circuit: {e}")
		except Exception as e:
			print(f'TorClient: {e}')
