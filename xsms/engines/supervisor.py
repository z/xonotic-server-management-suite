import subprocess
import os


def start(servers):
    """
    This engine enables pass-through control of servers managed by supervisor

    :param servers:

    >>> import yaml
    >>> from xsms.engines import supervisor
    >>> from xsms.config import conf
    >>> with open(conf['servers_manifest']) as f:
    >>>     servers = yaml.load(f)
    >>> supervisor.start(servers=servers)
    """
    if not os.path.exists('/etc/supervisor/conf.d/supervisord.conf'):
        print('Unable to locate /etc/supervisor/conf.d/supervisord.conf')
        raise SystemExit

    for server in servers['servers']:
        print(server)
        p = subprocess.Popen(['supervisorctl', 'start', server], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
