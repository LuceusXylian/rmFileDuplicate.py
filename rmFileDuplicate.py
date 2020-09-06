#!/usr/bin/env python2
import subprocess
import os


RM_FILEEXTENTION = 'm4a'

matches = subprocess.check_output("find . -exec bash -c 'basename \"$0\" \".${0##*.}\"' {} \; | sort | uniq --repeated", shell=True).split("\n")

for match in matches:
    print(match)
    os.system('rm "'+match+'.'+RM_FILEEXTENTION+'"')