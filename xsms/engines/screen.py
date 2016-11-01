import screenutils
from xsms.engine import Engine
"""
Created on Oct 30, 2016
@author: Tyler Mulligan
"""


class Session(Engine):
    """
    This is the ``engine`` class for ``screen``
    """

    def start(self, xonotic_root, servers_manifest=None):
        """
        This engine enables programmatic control of ``screen``

        :param xonotic_root: The directory for the ``exec`` command
        :type xonotic_root: ``str``

        :param servers_manifest: A file in the ``servers.yml`` format
        :type servers_manifest: ``str``

        >>> from xsms.engines.screen import Session as screen
        >>> from xsms.config import conf
        >>> session = screen(conf=conf)
        >>> servers = session.start(xonotic_root=conf['xonotic_root'])
        """

        screen_sessions = {}

        for server in self.servers:
            screen_sessions[server] = screenutils.Screen(server.name, True)
            screen_sessions[server].send_commands('cd {0}'.format(xonotic_root))
            screen_sessions[server].send_commands(server.exec)

        screenutils.list_screens()
