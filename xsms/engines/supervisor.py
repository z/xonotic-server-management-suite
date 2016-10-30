import subprocess
import os


def start(servers, xonotic_root):
    if not os.path.exists('/etc/supervisor/conf.d/supervisord.conf'):
        print('Unable to locate /etc/supervisor/conf.d/supervisord.conf')
        raise SystemExit

    for server in servers['servers']:
        print(server)
        p = subprocess.Popen(['supervisorctl', 'start', server], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
