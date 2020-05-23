import os
import sys
import subprocess
import shlex
from termcolor import colored

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def send_cmd(command):
    print(command)
    result_str =os.popen(command).read()
    print(result_str)
    return result_str

print(os.getcwd())
print(os.listdir(os.getcwd()))

send_cmd('chmod +x {0:s}/my_marlin/buildroot/bin/*'.format(os.getcwd()))
sys.path.append('{0:s}/my_marlin/buildroot/bin'.format(os.getcwd()))
print(sys.path)
os.chdir('my_marlin')

# replaceAll(mk_path, "#webrepl.start()","import machine;".format(str))

subprocess.call(['{0:s}/buildroot/bin/restore_configs'.format(os.getcwd())])
########################################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set MOTHERBOARD {1:s}'.format(os.getcwd(), os.environ['BOARD'])))
print(colored('The select board is {0:s}'.format(os.environ['BOARD']), "green"))
########################################################################################################################

########################################################################################################################

########################################################################################################################

str = '0000'
if None != str:
    send_cmd('echo ::set-output name=RESULT::{0:s}'.format(str))

