import os
from mmap import *


cave_dir = r'D:\hollows_hunter64\out\scan_1673467013\process_8420.int'

def mmap_io_find(filename: str, what: str):
    with open(filename, mode="rb") as f:
        with mmap(f.fileno(), length=0, access=ACCESS_READ) as m:
            index = 1
            while index > 0:
                index = m.find(bytes(what, 'utf-8'))
                if index > 0:
                    try:
                        print(f'[+] @{index} [{str(m[index:index + 10])}]' +
                              f'[{m[index:index + 10].decode("utf-8").strip()}]'
                              )
                    except Exception as e:
                        print(f'[!] convert: {e}')
                m.seek(index + 1)

def main():
    try:
        files = os.listdir(cave_dir)
        print(f'processing {cave_dir} ({len(files)})')
        num = 0
        
        for f in files:
            num += 1
            size = os.path.getsize(os.path.join(cave_dir, f))
            print(f'[f] #{num} {f}, {size / 1024.0 / 1024.0:.2f} Mb')
            
            mmap_io_find(os.path.join(cave_dir, f), "reland")
    except Exception as e:
        print(f'exception: {e}')

if __name__ == '__main__':
    main()
