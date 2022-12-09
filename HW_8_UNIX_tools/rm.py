#!/usr/bin/env python3

import os
import sys
import argparse


def parse_rm_args():
    parser = argparse.ArgumentParser(
        usage='rm.py [OPTION] [FILE]',
        description='''Remove (unlink) the FILE(s).''',
        epilog='''By default, rm does not remove directories. 
        Use the --recursive (-r or -R) option to remove each listed directory, too, along with all of its contents.\n
        To remove a file whose name starts with a '-', for example '-foo', use one of these commands:\n
        rm -- -foo\n
        rm ./-foo
        ''')

    parser.add_argument('-r', '--recursive', action='store_true',
                        help='remove directories and their contents recursively',
                        required=False)

    parser.add_argument('files', type=str, default=None, nargs='*',
                        help='files to delete')
    return parser.parse_args()


if __name__ == '__main__':
    del_functions = {False: os.remove,
                     True: os.rmdir}

    args = parse_rm_args()

    for file in args.files:
        try:
            is_dir = args.recursive and os.path.isdir(file)
            del_functions[is_dir](file)
        except (NotADirectoryError, FileNotFoundError):
            sys.stderr.write(f'rm: cannot remove \'{file}\': No such file or directory\n')
        except IsADirectoryError:
            sys.stderr.write(f'rm: cannot remove \'{file}\': Is a directory\n')
