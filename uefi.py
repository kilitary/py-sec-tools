#  Copyright 2022 Sergey Efimov (kilitary@gmail.com)

import uefi_firmware


with open('D:\\temp\\bios_f51\\B450MS2H.F51', 'r') as fh:
    file_content = fh.read()
parser = uefi_firmware.AutoParser(file_content)
if parser.type() != 'unknown':
    firmware = parser.parse()
    firmware.showinfo()
