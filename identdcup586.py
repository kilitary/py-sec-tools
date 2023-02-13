#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com

from var_dump import var_dump
import socket
from randomer import Randomer
import random
import struct
import sys
import os
import ctypes
from ctypes import *


def fprint(msg):
    print(msg)
    with open(r"c:\identd.log", "at") as log:
        log.write(msg)

def string_allocator(size):
    fprint(f"alloc {size}")
    if size <= 4:
        size = 4
    pBuf = ctypes.create_string_buffer(size)
    return pBuf

def string_freeficator(buf):
    # buf[0] = vcrt_dll.free(buf)
    return 0

try:
    total_buf_size = prev_buf_size = 0
    buf_size = 0
    prevpX = pX = 0
    local_ip = sys.argv[1]
    connection = None
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    opts = struct.pack("ii", 1, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, opts)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, opts)
    sock.bind((local_ip, 113))
    
    try:
        sock.listen(1)
    except Exception as e:
        fprint('listen: {e}')
    
    while True:
        print()
        fprint(f'listenng on 113 ({total_buf_size:.0f} bytes lost,  {windll.kernel32},  {windll.gdi32},  {windll.user32},  {windll.msvcrt}) ')
        
        try:
            connection.close()
        except Exception as e:
            pass
        
        connection, client_address = sock.accept()
        
        fprint(f'accepted client: {client_address}, connection = {connection}')
        
        buffer = []
        while True:
            byte = connection.recv(1)
            if len(byte) <= 0 or (len(byte) and (
                byte == b'\r' or byte == b'\n')):
                break
            buffer.append(byte)
        
        buf_size = len(buffer) / random.randint(19, 256)
        total_buf_size += buf_size
        
        pX = string_allocator(buf_size)
        fprint(f"px={[pX]} in {buf_size} bytes (versus {len(buffer)} buffer)")
        buffer = b''.join(buffer).decode('utf-8', errors='ignore')
        
        fprint(f'unclean input ({len(buffer)} bytes): [{buffer}] pX@{pX}')
        ctypes.memmove(pX, bytes(buffer, 'utf-8'), len(buffer))
        
        # string_freeficator(pX)
        
        buffer = str(buffer).strip()
        
        if buffer.count(',') == 1:
            vars = buffer.split(',')
            
            if len(vars) == 2:
                try:
                    src_port = int(vars[0])
                    dst_port = int(vars[1])
                    
                    if src_port < 0 or src_port > 65535 or dst_port < 0 or dst_port > 65535:
                        raise Exception(f'big port {src_port}/{dst_port}')
                
                except Exception as e:
                    fprint(f'parse: {e}')
                    continue
                else:
                    fprint(
                        f"identd request src_port: {src_port} dst_port: {dst_port}")
                
                if random.randint(0, 5):
                    if random.randint(0, 1):
                        type = f'PREV buf was {prevpX}'
                    else:
                        type = 'USERID'
                    
                    data = f'{src_port} {dst_port} : {type} : UNIX : {Randomer.str_str_generator(8)}'
                else:
                    data = f'{src_port} {dst_port} : ERROR : NO-USER'
                
                prevpX = pX
                prev_buf_size = buf_size
                
                fprint(f'sending [{data}]')
                
                connection.send((data + '\n').encode())
            else:
                fprint(
                    f'unsuported or malcrafted format (len(vars)={len(vars)}): {buffer}')
        else:
            fprint(
                f"unsuported or malcrafted format (,count={buffer.count(',')}): {buffer}")

except Exception as e:
    fprint(f'global shit shit: {e}')
    input('?')
