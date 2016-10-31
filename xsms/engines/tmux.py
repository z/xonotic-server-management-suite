import libtmux
import subprocess
from xsms.engine import Engine
"""
Created on Oct 30, 2016
@author: Tyler Mulligan
"""


class Session(Engine):
    """
    This is the ``engine`` class for ``tmux``
    """

    def start(self, xonotic_root, servers_manifest=None):
        """
        This engine enables programmatic control of ``tmux``

        :param xonotic_root: The directory for the ``exec`` command
        :type xonotic_root: ``str``

        :param servers_manifest: A file in the ``servers.yml`` format
        :type servers_manifest: ``str``

        >>> from xsms.engines.tmux import Session as tmux
        >>> from xsms.config import conf
        >>> session = tmux(conf=conf)
        >>> servers = session.start()

        .. note::
            This tries to create a new session with Popen() but it
            does not always work. It is therefore better to already
            have a tmux session running before using this command.
        """

        server = libtmux.Server()
        p = subprocess.Popen(['tmux', 'new-session', '-s', 'xsms', '-n', 'main'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        session = server.find_where({"session_name": 'xsms'})

        for server in self.servers['servers']:
            session.new_window(attach=False, window_name=server, start_directory=xonotic_root,
                               window_shell=self.servers['servers'][server]['exec'])
