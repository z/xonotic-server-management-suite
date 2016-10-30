import yaml
import os
from datetime import datetime
from xsms.engines import screen
from xsms.engines import tmux
"""
Created on Oct 30, 2016
@author: Tyler Mulligan
"""


class ServersCommand:
    """This class handles the `xsms servers` subcommand

    :param conf:
        The conf dictionary from `config.py`
    :type conf: ``dictionary``

    .. note::
        This file is subject to change with the addition of new
        engines until and API has been established.

    """

    def __init__(self, conf):
        self.conf = conf

    def generate_engine_configs(self):
        """
        This method generates **engine** configs
        """
        with open(self.conf['supervisor_server_template']) as f:
            template = f.read()
            template = '{0}\n\n'.format(template)

        with open(self.conf['servers_manifest']) as f:
            servers = yaml.load(f)

        current_date = datetime.now()

        supervisor_data = '# Last Generated: {}\n' \
                          '[supervisord]\n' \
                          'nodaemon=true\n'.format(current_date)

        for server in servers['servers']:
            supervisor_data += template.format(
                gs_name=server,
                gs_command=servers['servers'][server]['exec'],
                xonotic_root=self.conf['xonotic_root'],
            )

        with open(self.conf['supervisor_conf'], 'w') as f:
            f.write(supervisor_data)

    def generate_server_configs(self):
        """
        This method generates `cfg` **server** configs from `YAML`
        """
        with open(self.conf['xonotic_server_template']) as f:
            template = f.read()
            template = '{0}\n\n'.format(template)

        with open(self.conf['servers_manifest']) as f:
            servers = yaml.load(f)

        current_date = datetime.now()

        for server in servers['servers']:
            server_data = '// Last Generated: {}\n'.format(current_date)
            server_data += template.format(
                servername=server,
                title=servers['servers'][server]['title'],
                motd=servers['servers'][server]['motd'],
                port=servers['servers'][server]['port'],
                maxplayers=servers['servers'][server]['maxplayers'],
                net_address=servers['servers'][server]['net_address'],
            )

            server_template = '{}/{}.cfg.tpl'.format(self.conf['xsms_templates_servers_root'], server)

            if os.path.exists(server_template):
                with open(server_template) as f:
                    custom_server_data = f.read()
                    server_data += '// Custom Server Config\n\n' \
                                   '{0}\n'.format(custom_server_data)

            with open('{}/{}.cfg'.format(self.conf['xsms_generated_servers_root'], server), 'w') as f:
                f.write(server_data)

    def start(self, engine='screen'):
        """
        This method starts servers with an engine
        """
        with open(self.conf['servers_manifest']) as f:
            servers = yaml.load(f)

        # using screen
        if engine == 'screen':
            screen.start(servers=servers, xonotic_root=self.conf['xonotic_root'])

        # using supervisor
        if engine == 'tmux':
            tmux.start(servers=servers, xonotic_root=self.conf['xonotic_root'])