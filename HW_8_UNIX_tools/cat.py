#!/usr/bin/env python3

import os
import sys
import argparse
import glob


def parse_cat_args():
    parser = argparse.ArgumentParser(
        usage='cat.py [FILE]',
        description='''Concatenate FILE(s) to standard output. 
        With no FILE, or when FILE is -, read standard input.'''
    )

    parser.add_argument('files', default=None, nargs='*', help='read input from the files')
    return parser.parse_args()


def write_from_files(files):
    for file in files:
        try:
            with open(file, 'r') as f:
                for line in f:
                    sys.stdout.write(line)
        except IsADirectoryError:
            sys.stderr.write(f'cat: {file}: Is a directory\n')


if __name__ == '__main__':
    files = parse_cat_args().files
    if files:
        for file in files:
            if file == '-':
                [sys.stdout.write(line) for line in sys.stdin]
            else:
                matching_files = glob.glob(file)
                if not matching_files:
                    sys.stderr.write(f'cat: {file}: No such file or directory\n')
                else:
                    write_from_files(matching_files)
    else:
        [sys.stdout.write(line) for line in sys.stdin]
