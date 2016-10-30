from datetime import datetime
import screenutils
import yaml
import os


class ServersCommand:

    def __init__(self, conf):
        self.conf = conf

    def generate_engine_configs(self):
        with open(self.conf['supervisor_server_template']) as f:
            template = f.read()
            template = '{0}\n\n'.format(template)

        with open(self.conf['servers_manifest']) as f:
            servers = yaml.load(f)

        current_date = datetime.now()

        supervisor_data = 'Last Generated: {}' \
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
        with open(self.conf['xonotic_server_template']) as f:
            template = f.read()
            template = '{0}\n\n'.format(template)

        with open(self.conf['servers_manifest']) as f:
            servers = yaml.load(f)

        current_date = datetime.now()

        for server in servers['servers']:
            server_data = 'Last Generated: {}'.format(current_date)
            server_data += template.format(
                gs_name=server,
                gs_command=servers['servers'][server]['exec'],
                xonotic_root=self.conf['xonotic_root'],
            )

            server_template = '{}/{}.cfg.tpl'.format(self.conf['xsms_servers_config_root'], server)

            print(server_template)

            if os.path.exists(server_template):
                with open(server_template) as f:
                    custom_server_data = f.read()
                    print(custom_server_data)
                    server_data += '// Custom Server Config\n\n' \
                                   '{0}\n'.format(custom_server_data)

            with open('{}/{}.cfg'.format(self.conf['xsms_servers_config_root'], server), 'w') as f:
                f.write(server_data)

    def start(self):
        screen_sessions = {}

        with open(self.conf['servers_manifest']) as f:
            servers = yaml.load(f)

        for server in servers['servers']:
            # using screen
            screen_sessions[server] = screenutils.Screen(server, True)
            screen_sessions[server].send_commands('cd {0}'.format(self.conf['xonotic_root']))
            screen_sessions[server].send_commands(servers['servers'][server]['exec'])

        screenutils.list_screens()

        # TODO: using supervisor
