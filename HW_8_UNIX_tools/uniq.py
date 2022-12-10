#!/usr/bin/env python3

import sys
import os
import argparse


def parse_cat_args():
    parser = argparse.ArgumentParser(
        usage='uniq.py [FILE]',
        description='''Filter adjacent matching lines from INPUT (or standard input), writing to OUTPUT (or standard output).
        Matching lines are merged to the first occurrence.'''
    )

    parser.add_argument('file', default=None, nargs='?', help='read input from the file')
    return parser.parse_args()


def write_uniq_from_stdin():
    try:
        [sys.stdout.write(line) for line in sys.stdin]
    except KeyboardInterrupt:
        sys.exit(1)


def write_uniq_from_file(file):
    line_before = None
    with open(file, 'r') as f:
        for line in f:
            if line != line_before:
                sys.stdout.write(line)
            line_before = line


if __name__ == '__main__':
    file = parse_cat_args().file

    if not file or file == '-':
        write_uniq_from_stdin()
    else:
        try:
            write_uniq_from_file(file)
        except FileNotFoundError:
            sys.stderr.write(f'uniq: {file}: No such file or directory\n')
        except IsADirectoryError:
            sys.stderr.write(f'uniq: error reading \'{file}\'\n')
