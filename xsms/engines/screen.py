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

    def start(self, xonotic_root, filename=None):
        """
        This engine enables programmatic control of ``screen``

        :param xonotic_root: The directory for the ``exec`` command
        :type xonotic_root: ``str``

        :param filename: A file in the ``servers.yml`` format
        :type filename: ``str``

        >>> from xsms.engines.screen import Session as screen
        >>> from xsms.config import conf
        >>> session = screen(conf=conf)
        >>> servers = session.start(xonotic_root=conf['xonotic_root'])
        """

        screen_sessions = {}

        for server in self.servers['servers']:
            screen_sessions[server] = screenutils.Screen(server, True)
            screen_sessions[server].send_commands('cd {0}'.format(xonotic_root))
            screen_sessions[server].send_commands(self.servers['servers'][server]['exec'])

        screenutils.list_screens()
