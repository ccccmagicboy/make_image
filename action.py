import os
import sys
from termcolor import colored

def send_cmd(command):
    print(command)
    result_str =os.popen(command).read()
    print(result_str)
    return result_str

OFFSET_BOOTLOADER = int(os.environ['BOOTLOADER_OFFSET'], 16)

files_in = [
    ('bootloader', OFFSET_BOOTLOADER, os.environ['BOOTLOADER_PATH']),
    ('application', int(os.environ['MARLIN_OFFSET'], 16), os.environ['MARLIN_PATH']),
]

file_out = os.environ['FILE_OUTPUT_NAME']

cur_offset = OFFSET_BOOTLOADER
with open(file_out, 'wb') as fout:
    for name, offset, file_in in files_in:
        assert offset >= cur_offset
        fout.write(b'\xff' * (offset - cur_offset))
        cur_offset = offset
        with open(file_in, 'rb') as fin:
            data = fin.read()
            fout.write(data)
            cur_offset += len(data)
            print(colored('%-12s% 8d' % (name, len(data)), "green"))
    print(colored('%-12s% 8d' % ('total', cur_offset), "green"))

str = '0001'
if None != str:
    send_cmd('echo ::set-output name=RESULT::{0:s}'.format(str))

