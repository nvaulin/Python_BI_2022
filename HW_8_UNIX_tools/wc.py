#!/usr/bin/env python3

import sys
import argparse


def parse_wc_args():
    parser = argparse.ArgumentParser(
        usage='wc.py [OPTION] [FILE]',
        description='''Print newline, word, and byte counts for FILE.  A word is a non-zero-length sequence of characters delimited by white space.
        With no FILE, or when FILE is -, read standard input. If not in pipe, reading from standard input finished with Ctrl + D''')

    parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts', required=False)
    parser.add_argument('-w', '--words', action='store_true', help='print the character counts', required=False)
    parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts', required=False)
    parser.add_argument('input_data', type=argparse.FileType('r'), default=sys.stdin, nargs='?',
                        help='Read input from the file')
    return parser.parse_args()


def extract_actions_list(args):
    del args['input_data']
    if not any(args.values()):
        return list(args.keys())
    else:
        return [action for action, is_needed in args.items() if is_needed]


def count_lines(data):
    return data.count("\n")


def count_words(data):
    return len(data.split())


def count_bytes(data):
    return sys.getsizeof(data) - sys.getsizeof('')


if __name__ == '__main__':
    args = parse_wc_args()
    input_data = args.input_data.read()
    actions = extract_actions_list(vars(args))

    functions = {'lines': count_lines,
                 'words': count_words,
                 'bytes': count_bytes
                 }

    results = []
    for action in actions:
        results.append(functions[action](input_data))

    sys.stdout.write('\t' + '\t'.join(map(str, results)) + '\n')
