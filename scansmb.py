#!/usr/bin/python
#
# ScanNetworkForSMB.py - Script for scanning network for open SMB/CIFS services
# Copyright (C) 2012 Michael Teo <miketeo (a) miketeo.net>
#
# This software is provided 'as-is', without any express or implied warranty.
# In no event will the author be held liable for any damages arising from the
# use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
#
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
#
# 3. This notice cannot be removed or altered from any source distribution.
#
import re
import errno
import sys, select, socket, random, string, time
from socket import AF_INET
import psutil
import os
import six
from var_dump import *
from pprint import *
import win32ui
from nmb import base
from helpers import deb, dir_files
from psutil import *

class NonBlockingNetBIOS(base.NBNS):
    
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        self.pendings = set()
        self.pending_count = 0
        
        self.servers = {}
    
    def write(self, data, ip, port):
        assert self.sock, 'Socket is already closed'
        
        try:
            self.sock.sendto(data, (ip, port))
        # deb(f'sendto({data.hex()}, {ip}, {port}) => {len}')
        except Exception as e:
            deb(f'sendto({data.hex}, {ip}, {port}) exception: {e}')
    
    def queryIPForName(self, ip):
        assert self.sock, 'Socket is already closed'
        
        trn_id = random.randint(1, 0xFFFF)
        deb(f'transaction {hex(trn_id)}')
        data = self.prepareNetNameQuery(trn_id)
        self.write(data, ip, 137)
        self.pendings.add(ip)
        self.pending_count += 1
    
    def queryResult(self, ip, results):
        # deb(f'results={results}')
        results = filter(lambda name: name[0], results)
        for r in results:
            if ip not in self.servers or not isinstance(self.servers[ip], list):
                self.servers[ip] = []
            elif r[0] not in self.servers[ip]:
                self.servers[ip].append(r[0])
    
    # deb(ip.rjust(16) + ' --> ' + '|'.join(results))
    
    def poll(self, timeout=0):
        end_time = time.time() + timeout
        while self.pending_count > 0 and (timeout == 0 or time.time() < end_time):
            t = max(0, int(end_time - time.time()))
            try:
                ready, _, _ = select.select([self.sock.fileno()], [], [], t)
                if not ready:
                    return None
                
                try:
                    data, (ip, port) = self.sock.recvfrom(0xFFFF)
                    deb(f"recvfrom(ip:{ip}, port:{port}) = '{data.hex()}'")
                except Exception as e:
                    deb(f'recvfrom({self.sock}): {e}')
                
                if 'data' not in locals():
                    continue
                
                _, ret = self.decodeIPQueryPacket(data)
                
                if 'ip' in locals() and ip in self.pendings:
                    self.pendings.remove(ip)
                    self.pending_count -= 1
                if ret is None:
                    deb(f'decodeIPQueryPacket() _={_} ret=null')
                else:
                    self.queryResult(ip, set(ret))
            
            except select.error as ex:
                if type(ex) is win32ui.types.TupleType:
                    if ex[0] != errno.EINTR and ex[0] != errno.EAGAIN:
                        raise ex
                else:
                    raise ex

# Originally from http://snipplr.com/view/14807/
def ip_to_int(dotted_ip):
    exp = 3
    intip = 0
    for quad in dotted_ip.split('.'):
        intip = intip + (int(quad) * (256 ** exp))
        exp -= 1
    return intip

def int_to_ip(intip):
    octet = ''
    for exp in [3, 2, 1, 0]:
        octet = octet + str(int(intip / (256 ** exp))) + "."
        intip = intip % (256 ** exp)
    
    return octet.rstrip('.')

def main():
    if len(sys.argv) > 2:
        start_ip = ip_to_int(sys.argv[1])
        end_ip = ip_to_int(sys.argv[2])
    elif len(sys.argv) == 2:
        start_ip = ip_to_int(sys.argv[1])
        end_ip = start_ip
    else:
        deb('ScanNetworkForSMB - Script for scanning network for open SMB/CIFS services')
        deb('Error: missing IP arguments')
        deb('Usage:' + sys.argv[0] + 'start-IP-address [end-IP-address]')
        return
    
    ifs = net_if_addrs()
    scan_networks = [sys.argv[1], sys.argv[1]]
    # var_dump(ifs, '-----')
    # for iface in ifs:
    # 	if ifs[iface][1].family == AF_INET:
    # 		scan_networks.append(ifs[iface][1].address)
    # var_dump(scan_networks)
    # deb(f'Beginning scanning %d IP addresses [{sys.argv[1]} - ] ... {(end_ip - start_ip + 1)}')
    
    for network in scan_networks:
        deb(f'scanning network {network} ... ', end='')
        
        starting = re.sub(r'^(\d+\.\d+\.\d+)\.\d+?$', r'\1.1', network, 0, re.DOTALL)
        ending = re.sub(r'^(\d+\.\d+\.\d+)\.\d+?$', r'\1.255', network, 0, re.DOTALL)
        
        deb(f'{starting} - {ending} ')
        
        start_ip = ip_to_int(starting)
        end_ip = ip_to_int(ending)
        
        ns = NonBlockingNetBIOS()
        for ip in range(start_ip, end_ip):
            ns.queryIPForName(int_to_ip(ip))
        ns.poll(4)
        
        if ns.pending_count > 0:
            ns.poll(4)
        
        var_dump(ns.servers)
        for ips in ns.servers:
            for token in ns.servers[ips]:
                deb(f'token {token}')
                ret = os.system(f'net use \\\\{token}')
                deb(f'net use -> {ret}')
                files = dir_files(r'\\' + token + r'\*')
                var_dump(files)
                sys.exit(0)
        
        deb('Query timeout. No replies from %d IP addresses' % ns.pending_count)

if __name__ == '__main__':
    main()
