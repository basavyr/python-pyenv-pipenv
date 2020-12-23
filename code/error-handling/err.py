#!/Users/robertpoenaru/.pyenv/shims/python
import subprocess
import os
import datetime
import time


def printer(l):
    counter = 1
    for x in l:
        print(f'{x}')
        # print(f'{counter}: {x}')
        counter = counter+1


logs = []

# for _ in range(10):
timestamp = str(datetime.datetime.utcnow())[0:19]
try:
    # raw_output = subprocess.check_output(['ls', './dir'], stderr=subprocess.PIPE)
    raw_output = subprocess.Popen(
        ['ls', '-la'],  stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = raw_output.communicate()
except subprocess.CalledProcessError as e:
    logs.append(f'{timestamp} err_msg=> [{str(e.stderr.decode()).strip()}]')
else:
    print(out.decode())
    # logs.append(f'{timestamp} err_msg=> [{str(e.stderr.decode()).strip()}]')


with open('logs.log', 'w') as filer:
    for log_line in logs:
        filer.write(log_line)
        filer.write('\n')
# try:
# 	f=open('file.txt','r')
# except OSError as e:
# 	print(f'Opening file failed due to the following error(s):')
# 	print(e)
# finally:
# 	print('Program finished the file opening')
