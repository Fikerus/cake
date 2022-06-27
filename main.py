#!/usr/bin/python3

import os


cakefile = ''
filename = ''

with os.popen('ls') as s:
    ls = [x[:-1] for x in s]
    if '.cake' in ls:
        filename = '.cake'
    if 'Cakefile' in ls:
        filename = 'Cakefile'

with open(filename,'r') as f:
    cakefile = f.read()

show_f = False

for command in (commands := [x for x in cakefile.split('\n') if x]):
    comment_f = command.startswith('#')

    if comment_f and command[1:]=='show':
        show_f = True

    if not(comment_f) and show_f:
        print(command)

    os.system(command)
