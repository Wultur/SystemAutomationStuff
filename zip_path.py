#!/usr/bin/python3


import os
import time
import sys

path_to_zip = sys.argv[1]
source = [path_to_zip]
target_dir = path_to_zip
now = time.strftime('%Y%m%d')
comment = input('Input name of file for Backup: ')
if len(comment) == 0:
    target = target_dir + os.sep + now + '.zip'
else:
    target = target_dir + os.sep + comment.replace(' ', '_') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup is successful in', target)
else:
    print('Error. Something go wrong.')
