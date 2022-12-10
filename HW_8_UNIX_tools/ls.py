#!/usr/bin/env python3

import os
import sys
import argparse


def parse_ls_args():
    parser = argparse.ArgumentParser(
        usage='ls.py [OPTION] [FILE]',
        description='''List the FILEs (the current directory by default). Sort entries alphabetically''')

    parser.add_argument('-a', '--all', action='store_true', help='do not ignore entries starting with .',
                        required=False)
    parser.add_argument('directory', type=str, default='.', nargs='?',
                        help='directory which content to display ("." by default)')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_ls_args()
    directory = args.directory

    try:
        dir_content = list(sorted(os.listdir(directory)))
        if args.all:
            dir_content.extend(['.', '..'])
        else:
            dir_content = list(filter(lambda x: not x.startswith('.'), dir_content))
        sys.stdout.write('  '.join(dir_content) + '\n')
    except FileNotFoundError:
        sys.stderr.write(f'ls: cannot access \'{directory}\': No such file or directory\n')
