class Server:
    """This class defines the Server object

    :param name:
        A name for the collection of servers
    :type name: ``str``

    :param exec:
        The executable line for when this server starts
    :type exec: ``str``

    :param title:
        The title of this server
    :type title: ``str``

    :param motd:
        The message of the day for this server
    :type motd: ``str``

    :param port:
        The port this server is served on
    :type port: ``str``

    :param maxplayers:
        The maximum number of players of this server
    :type maxplayers: ``int``

    :param net_address:
        The ip address of this server
    :type net_address: ``str``

    :param use_smbmod:
        Whether this server uses SMB Modpack or not
    :type use_smbmod: ``bool``

    :returns object: ``Server``

    :Example:

    >>> from xsms.server import Server
    >>> server = Server(name='insta', exec='./all run dedicated +serverconfig vanilla.cfg', title='My server')
    """
    def __init__(self, name, exec, title, motd='Welcome to ${hostname}!', port='26000', maxplayers='32', net_address='', use_smbmod=True):
        self.name = name
        self.exec = exec
        self.title = title
        self.motd = motd
        self.port = port
        self.maxplayers = maxplayers
        self.net_address = net_address
        self.use_smbmod = use_smbmod

    def __repr__(self):
        return '<Server ({0.name}, "{0.exec}", "{0.title}", "{0.motd}", {0.port}, {0.maxplayers}, {0.net_address}, {0.use_smbmod})>'.format(self)


class Servers:
    """This class defines the Servers object

    :param name:
        A name for the collection of servers
    :type name: ``str``

    :param servers:
        A list of ``Server`` objects
    :type servers: ``list``

    :returns object: ``Servers``

    :Example:

    >>> from xsms.server import Servers, Server
    >>> server = Server(name='insta', exec='./all run dedicated +serverconfig vanilla.cfg', title='My server')
    >>> servers = Servers(name='Xonotic Server Collection', servers=[server])
    """

    def __init__(self, name, servers=None):
        self.name = name
        self.servers = []

        if servers and isinstance(servers, list):
            for server in servers:
                self.add_server(server)

    def __repr__(self):
        return '<Servers ({0.name}, {0.servers})>'.format(self)

    def add_server(self, server):
        if isinstance(server, Server):
            self.servers.append(server)
        else:
            raise Exception('Failed to add server')
