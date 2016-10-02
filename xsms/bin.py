#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
import argparse
import subprocess
import os


def main():
    args = parse_args()

    conf = {
        'init_script': os.path.expanduser('bin/init.sh'),
        'update_script': os.path.expanduser('~/.xonotic-smb/modpack/update.sh'),
        'build_script': os.path.expanduser('~/.xonotic-smb/modpack/build.sh'),
        'smb_cache_path': os.path.expanduser('~/.xonotic-smb/modpack/.cache'),
        'data_csprogs': os.path.expanduser('~/.xonotic-smb/data_csprogs'),
    }

    if args.command == 'smbmod':

        if args.subcommand == 'init':
            # Until refactored
            subprocess.call([conf['init_script']])

        if args.subcommand == 'update':
            subprocess.call([conf['update_script']])

        if args.subcommand == 'build':
            subprocess.call([conf['build_script']])

        if args.subcommand == 'sync':

            if args.all:
                subprocess.call([conf['update_script']])
                subprocess.call([conf['build_script']])

            subprocess.call(['rsync', '-azvh', conf['smb_cache_path'], conf['data_csprogs']])


def parse_args():

    parser = argparse.ArgumentParser(description='Xonotic Server Management Suite is a tool to help manage Xonotic servers.')

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    parser_smbmod = subparsers.add_parser('smbmod', help='take actions related to the SMB mod')
    parser_smbmod.add_argument('subcommand', choices=['init', 'build', 'update', 'sync'], type=str)
    parser_smbmod.add_argument('--all', '-A', help='Sync smb mod and build as well?', action='store_true')

    return parser.parse_args()

if __name__ == '__main__':
    main()
