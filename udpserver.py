import socket

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

sock.bind(("192.168.0.3", 54))

def fprint(msg):
	print(msg)
	with open("log.txt", "at") as log:
		log.write(msg)

while True:
	data, addr = sock.recvfrom(65535)  # buffer size is 1024 bytes
	fprint(f"{addr}: {data}")
