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
        This reads in a ``servers.yml`` file, turns it into a dict.
        sets ``self.servers`` to that value and then returns it.

        :param filename: A yaml file using the syntax of ``servers.yml``
        :type filename: ``str``

        :returns self: ``dict``
            A dict of servers as defined in ``servers.yml``

        >>> from xsms.engine import Engine
        >>> from xsms.config import conf
        >>> session = Engine(conf=conf)
        >>> servers = session.read_servers_manifest(filename=conf['servers_manifest'])
        """

        with open(filename) as f:
            self.servers = yaml.load(f)

        return self.servers
