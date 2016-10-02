#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
import argparse
import subprocess
import shlex
import yaml
from xsms.config import conf


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

            subprocess.call(['rsync', '-azvh', conf['smb_cache_path'], conf['data_csprogs']])

    if args.command == 'servers':

        if args.subcommand == 'run':
            with open(conf['servers_manifest']) as f:
                data = yaml.load(f)
                for server in data['servers']:
                    run_cmd = shlex.split(data['servers'][server]['exec'])
                    subprocess.call(run_cmd)


def parse_args():

    parser = argparse.ArgumentParser(description='Xonotic Server Management Suite is a tool to help manage Xonotic servers.')

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    parser_smbmod = subparsers.add_parser('smbmod', help='take actions related to the SMB mod')
    parser_smbmod.add_argument('subcommand', choices=['init', 'build', 'update', 'sync'], type=str)
    parser_smbmod.add_argument('--all', '-A', help='Sync smb mod and build as well?', action='store_true')

    parser_servers = subparsers.add_parser('servers', help='take actions related to the servers')
    parser_servers.add_argument('subcommand', choices=['run'], type=str)

    return parser.parse_args()

if __name__ == '__main__':
    main()
