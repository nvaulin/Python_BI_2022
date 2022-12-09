#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path


def parse_mkdir_args():
    parser = argparse.ArgumentParser(
        usage='mkdir.py [OPTION] [DIRECTORY] ...',
        description='''Create the DIRECTORY(ies), if they do not already exist. 
        ''')

    parser.add_argument('-p', '--parent', action='store_true', help='make symbolic links instead of hard links',
                        required=False)
    parser.add_argument('directory', default=None, nargs='*', help='')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_mkdir_args()

    for directory in args.directory:
        try:
            Path.mkdir(directory, parents=args.parent, exist_ok=False)
        except FileNotFoundError:
            sys.stderr.write(f'mkdir: cannot create directory \'{directory}\': No such file or directory ')
        except FileExistsError:
            sys.stderr.write(f'mkdir: cannot create directory \'{directory}\': File exists ')
