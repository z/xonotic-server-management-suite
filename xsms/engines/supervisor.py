import subprocess
import os
from xsms.engine import Engine
"""
Created on Oct 30, 2016
@author: Tyler Mulligan
"""


class Session(Engine):
    """
    This is the ``engine`` class for ``supervisor``
    """

    def start(self, servers_manifest=None):
        """
        This engine enables pass-through control of servers managed by ``supervisor``.

        :param servers_manifest: A file in the ``servers.yml`` format
        :type servers_manifest: ``str``

        >>> from xsms.engines.supervisor import Session as supervisor
        >>> from xsms.config import conf
        >>> session = supervisor(conf=conf)
        >>> servers = session.start()
        """

        if not os.path.exists('/etc/supervisor/conf.d/supervisord.conf'):
            print('Unable to locate /etc/supervisor/conf.d/supervisord.conf')
            raise SystemExit

        for server in self.servers:
            p = subprocess.Popen(['supervisorctl', 'start', server.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
