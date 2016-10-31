import yaml
"""
Created on Oct 30, 2016
@author: Tyler Mulligan
"""


class Engine:
    """
    This is the base class for ``engines``, the ``read_servers_manifest``
    is fired on init reading in `conf['servers_manifest']`.

    :param conf: A dict ``conf`` from ``config.py``
    :type conf: ``dict``
    """
    def __init__(self, conf):
        self.conf = conf
        self.servers = None
        self.read_servers_manifest(conf['servers_manifest'])

    def read_servers_manifest(self, filename):
        """
        This reads in a ``servers.yml`` file, turns it into a dictionary.
        sets ``self.servers`` to that value and then returns it.

        :param filename: A yaml file using the syntax of ``servers.yml``
        :type filename: ``string``

        :returns self: ``dict``
            A dictionary of servers as defined in ``servers.yml``

        .. note::
            This tries to create a new session with Popen() but it
            does not always work. It is therefore better to already
            have a tmux session running before using this command.

        >>> from xsms.engine import Engine
        >>> from xsms.config import conf
        >>> session = Engine(conf=conf)
        >>> servers = session.read_servers_manifest(filename=conf['servers_manifest'])
        """

        with open(filename) as f:
            self.servers = yaml.load(f)

        return self.servers
