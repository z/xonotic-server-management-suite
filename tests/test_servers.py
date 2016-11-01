import os
from xsms.server import Servers
from xsms.server import Server
from xsms.config import conf

root_dir = os.path.dirname(os.path.abspath(__file__))


def test_server_object():
    server = Server(name='insta', exec='./all run dedicated +serverconfig vanilla.cfg', title='My server')
    assert server.name == 'insta'


def test_servers_object():
    server1 = Server(name='vanilla', exec='./all run dedicated +serverconfig vanilla.cfg', title='My server 1')
    server2 = Server(name='insta', exec='./all run dedicated +serverconfig insta.cfg', title='My server 2')
    servers = Servers(name='Xonotic Server Collection', servers=[server1, server2])
    assert servers.servers[0].name == 'vanilla'
    assert servers.servers[1].title == 'My server 2'
