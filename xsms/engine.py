import yaml
from xsms.server import Server
from xsms.server import Servers
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

    :returns: ``Engine``
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

        :returns: ``Servers``

        >>> from xsms.engine import Engine
        >>> from xsms.config import conf
        >>> session = Engine(conf=conf)
        >>> servers = session.read_servers_manifest(filename=conf['servers_manifest'])
        """

        servers = Servers(name='default')

        with open(filename) as f:
            servers_manifest = yaml.load(f)

        for server in servers_manifest['servers']:

            this_server = Server(
                name=server,
                exec=servers_manifest['servers'][server]['exec'],
                title=servers_manifest['servers'][server]['title'],
                motd=servers_manifest['servers'][server]['motd'],
                port=servers_manifest['servers'][server]['port'],
            )

            if 'port' in servers_manifest['servers'][server]:
                this_server.maxplayers = servers_manifest['servers'][server]['port']

            if 'maxplayers' in servers_manifest['servers'][server]:
                this_server.maxplayers = servers_manifest['servers'][server]['maxplayers']

            if 'net_address' in servers_manifest['servers'][server]:
                this_server.net_address = servers_manifest['servers'][server]['net_address']

            if 'use_smbmod' in servers_manifest['servers'][server]:
                this_server.use_smbmod = servers_manifest['servers'][server]['use_smbmod']

            servers.add_server(this_server)

        self.servers = servers.servers

        return servers
