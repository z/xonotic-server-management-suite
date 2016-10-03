#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
import argparse
import subprocess
import shlex
import yaml
import screenutils
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

            subprocess.call(['rsync', '-azvh', conf['smb_cache_path'] + '/', conf['data_csprogs']])

    if args.command == 'servers':

        if args.subcommand == 'start':

            screen_sessions = {}

            with open(conf['servers_manifest']) as f:
                servers = yaml.load(f)

            for server in servers['servers']:
                # using screen
                screen_sessions[server] = screenutils.Screen(server, True)
                screen_sessions[server].send_commands(servers['servers'][server]['exec'])

            screenutils.list_screens()

            # TODO: using supervisor

        # supervisor conf needs to be generated if using supervisor
        if args.subcommand == 'build':

            with open(conf['supervisor_server_template']) as f:
                template = f.read()
                template = '{0}\n\n'.format(template)

            with open(conf['servers_manifest']) as f:
                servers = yaml.load(f)

            supervisor_data = ''

            for server in servers['servers']:
                supervisor_data += template.format(
                        gs_name=server,
                        gs_command=servers['servers'][server]['exec'],
                        xonotic_root=conf['xonotic_root'],
                    )

            with open(conf['supervisor_conf'], 'w') as f:
                f.write(supervisor_data)


def parse_args():

    parser = argparse.ArgumentParser(description='Xonotic Server Management Suite is a tool to help manage Xonotic servers.')

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    parser_smbmod = subparsers.add_parser('smbmod', help='take actions related to the SMB mod')
    parser_smbmod.add_argument('subcommand', choices=['init', 'build', 'update', 'sync'], type=str)
    parser_smbmod.add_argument('--all', '-A', help='Sync smb mod and build as well?', action='store_true')

    parser_servers = subparsers.add_parser('servers', help='take actions related to the servers')
    parser_servers.add_argument('subcommand', choices=['start', 'build'], type=str)

    return parser.parse_args()

if __name__ == '__main__':
    main()
