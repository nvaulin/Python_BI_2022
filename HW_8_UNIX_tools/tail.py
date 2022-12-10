#!/usr/bin/env python3

import sys
import argparse
import glob


def parse_tail_args():
    parser = argparse.ArgumentParser(
        usage='cat.py [FILE] ...',
        description='''Print the last 10 lines of each FILE to standard output.                                                                             With more than one FILE, precede each with a header giving the file name.
        With no FILE, or when FILE is -, read standard input. '''
    )
    parser.add_argument('-n', '--lines', default=10, help='output the last NUM lines, instead of the last 10',
                        required=False)
    parser.add_argument('files', default=None, nargs='*', help='read input from the files')
    return parser.parse_args()


def write_lines(text):
    for row in text:
        sys.stdout.write(row)


def write_from_stdin(lines):
    text = sys.stdin.readlines()
    write_lines(text[-lines:])
    sys.stdout.write('\n')


def write_from_file(file, lines):
    try:
        with open(file, 'r') as f:
            text = f.readlines()
        write_lines(text[-lines:])
    except IsADirectoryError:
        sys.stderr.write(f'tail: error reading \'{file}\': Is a directory\n')


def write_namely(file, lines):
    sys.stdout.write(f'==> {file} <==\n')
    write_from_file(file, lines)
    sys.stdout.write('\n')


def find_matching_files(file):
    matching_files = []
    matching_files.extend(glob.glob(file))
    return matching_files


def write_from_matching_files(file, input_size, lines):
    matching_files = find_matching_files(file)
    match_size = len(matching_files)
    if matching_files:
        if match_size == 1 and input_size == 1:
            write_from_file(file, lines)
        else:
            for file in matching_files:
                write_namely(file, lines)
    else:
        sys.stderr.write(f'tail: {file}: No such file or directory\n')


if __name__ == '__main__':
    files = parse_tail_args().files
    lines = int(parse_tail_args().lines)
    input_size = len(files)

    if not files:
        write_from_stdin(lines)
    else:
        for file in files:
            if file == '-':
                if input_size > 1:
                    sys.stdout.write(f'==> standard input <==\n')
                write_from_stdin(lines)
            else:
                write_from_matching_files(file, input_size, lines)
