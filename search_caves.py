import os
import sys
from mmap import *
import pandas as pd
import json
from pprint import pprint
from capstone import *

cave_dir = r'H:\hollow-scan\scan_1673888423'
scan_report = {}
dump_report = {}

def mmap_io_find(filename: str, what: str):
    try:
        with open(filename, mode="rb") as file:
            try:
                with mmap(file.fileno(), length=0, access=ACCESS_READ) as mm:
                    search_file(mm, what)
            except Exception as e:
                print(f"\nmmap exception: {e}")
    except Exception as e:
        print(f"\nopen: {e}")

def search_file(mm: object, what):
    index = 1
    while index > 0:
        index = mm.find(bytes(what, 'utf-8'))
        if index > 0:
            try:
                print(
                    f"\n\r@{index} 0x{index:08x} [{str(mm[index:index + 10]).strip()}]" +
                    f'[{mm[index:index + 10].decode("utf-8").strip()}]'
                )
            except Exception as e:
                print(f"\n[!] search_file: {e}")
        mm.seek(index + 1)

def mmap_find(mmap_path, sign):
    try:
        mmap_io_find(mmap_path, sign)
    except Exception as e:
        print(f"\nmmap_io_find exception: {e}")

def read_json(path):
    with open(path, 'r') as f:
        r = json.load(f)
    return r

def scan_files(path):
    try:
        print(f'path: {scan_report["main_image_path"]}')
        
        num = 0
        files = os.listdir(path)
        for file in files:
            num += 1
            
            # pprint(report)
            # sys.exit()
            
            size = os.path.getsize(os.path.join(path, file))
            
            print(
                f"#{num} {file}, {size / 1024.0 / 1024.0:.2f} Mb" + (
                    " " * 50))
            mmap_path = os.path.join(path, file)
            mmap_find(mmap_path, "n3t1sn3t")
    
    except Exception as e:
        print(f"\ne: {e}")

def main():
    global scan_report, dump_report
    
    dirs = os.listdir(cave_dir)
    print(f'processing {cave_dir} ({len(dirs)})')
    
    for dir in dirs:
        if not os.path.isdir(os.path.join(cave_dir, dir)):
            continue
        
        path = os.path.join(cave_dir, dir)
        scan_report = read_json(os.path.join(path, 'scan_report.json'))
        dump_report = read_json(os.path.join(path, 'dump_report.json'))
        scan_files(path)

if __name__ == '__main__':
    main()
