# !/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line 2')
    if False:               # this is a comment
        print('line 3')     # this is another comment
    else:
        print('not true')

if __name__ == '__main__': main()
