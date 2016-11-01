import os
from xsms.engine import Engine
from xsms.server import Servers
from xsms.server import Server
from xsms.config import conf

root_dir = os.path.dirname(os.path.abspath(__file__))


def test_generate_engine_configs():
    session = Engine(conf=conf)
    servers = session.read_servers_manifest(filename=conf['servers_manifest'])
    assert isinstance(servers, Servers)
    assert isinstance(servers.servers[0], Server)
