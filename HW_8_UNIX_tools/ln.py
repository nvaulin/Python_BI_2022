#!/usr/bin/env python3

import os
import sys
import argparse


def parse_ln_args():
    parser = argparse.ArgumentParser(
        usage='ln.py [OPTION] [TARGET] [LINK_NAME]]',
        description='''Create hard links by default, symbolic links with --symbolic.
        By default, each destination (name of new link) should not already exist.
        When creating hard links, each TARGET must exist.  Symbolic links
        can hold arbitrary text; if later resolved, a relative link is
        interpreted in relation to its parent directory.''')

    parser.add_argument('-s', '--symbolic', action='store_true', help='make symbolic links instead of hard links',
                        required=False)
    parser.add_argument('target', help='', nargs='?')
    parser.add_argument('link_name', help='', nargs='?')
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_ln_args()
    target = args.target
    if os.path.isfile(target) or os.path.isdir(target):
        if args.symbolic:
            os.symlink(args.target, args.link_name)
        else:
            os.link(args.target, args.link_name)
    else:
        sys.stderr.write(f'ln: failed to access \'{target}\': No such file or directory\n')
