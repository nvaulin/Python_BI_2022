#!/usr/bin/env python3

import sys
import argparse


def parse_sort_args():
    parser = argparse.ArgumentParser(
        usage='sort.py [OPTION] [FILE]',
        description='''Write sorted concatenation of all FILE(s) to standard output.
        With no FILE, or when FILE is -, read standard input.''')

    parser.add_argument('input_files', type=argparse.FileType('r'), default=None, nargs='*',
                        help='read input from the files')
    return parser.parse_args()


if __name__ == '__main__':
    files = parse_sort_args().input_files
    if files:
        data = ''
        for file in files:
            data += file.read()
    else:
        data = sys.stdin.read()

    sorted_data = sorted(data.split('\n'))
    sys.stderr.write('\n'.join(map(str, sorted_data))[1:] + '\n')
