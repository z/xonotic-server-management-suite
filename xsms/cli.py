#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
import argparse
import subprocess
from .config import conf
from .__about__ import __version__
from .command import Command


def main():

    args = parse_args()

    if args.command == 'smbmod':

        if args.subcommand == 'init':
            # Until refactored
            subprocess.call([conf['smb_init_script']])

        if args.subcommand == 'update':
            subprocess.call([conf['smb_update_script']])

        if args.subcommand == 'build':
            subprocess.call([conf['smb_build_script']])

        if args.subcommand == 'sync':

            if args.all:
                subprocess.call([conf['smb_update_script']])
                subprocess.call([conf['smb_build_script']])

            subprocess.call(['rsync', '-azvh', conf['smb_cache_path'] + '/', conf['data_csprogs']])

    if args.command == 'servers':

        command = Command(conf=conf)

        if args.subcommand == 'start':
            command.start(engine=args.engine)

        # supervisor conf needs to be generated if using supervisor
        if args.subcommand == 'build':
            command.generate_engine_configs()
            command.generate_server_configs()


def parse_args():

    parser = argparse.ArgumentParser(description='Xonotic Server Management Suite is a tool to help manage Xonotic servers.')

    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    parser_smbmod = subparsers.add_parser('smbmod', help='take actions related to the SMB mod')
    parser_smbmod.add_argument('subcommand', choices=['init', 'build', 'update', 'sync'], type=str)
    parser_smbmod.add_argument('--all', '-A', help='Sync smb mod and build as well?', action='store_true')

    parser_servers = subparsers.add_parser('servers', help='take actions related to the servers')
    parser_servers.add_argument('subcommand', choices=['start', 'build'], type=str)
    parser_servers.add_argument('--engine', '-e', choices=['screen', 'tmux', 'supervisor'], help='What engine to start with')

    return parser.parse_args()

if __name__ == '__main__':
    main()
