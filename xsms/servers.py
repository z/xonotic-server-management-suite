import screenutils
import yaml


class ServersCommand:

    def __init__(self, conf):
        self.conf = conf

    def build(self):
        with open(self.conf['supervisor_server_template']) as f:
            template = f.read()
            template = '{0}\n\n'.format(template)

        with open(self.conf['servers_manifest']) as f:
            servers = yaml.load(f)

        supervisor_data = '[supervisord]\n' \
                          'nodaemon=true\n'

        for server in servers['servers']:
            supervisor_data += template.format(
                gs_name=server,
                gs_command=servers['servers'][server]['exec'],
                xonotic_root=self.conf['xonotic_root'],
            )

        with open(self.conf['supervisor_conf'], 'w') as f:
            f.write(supervisor_data)

    def start(self):
        screen_sessions = {}

        with open(self.conf['servers_manifest']) as f:
            servers = yaml.load(f)

        for server in servers['servers']:
            # using screen
            screen_sessions[server] = screenutils.Screen(server, True)
            screen_sessions[server].send_commands(servers['servers'][server]['exec'])

        screenutils.list_screens()

        # TODO: using supervisor
