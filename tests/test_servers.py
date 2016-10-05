import os
from xsms.servers import ServersCommand
from xsms.config import conf


def test_servers_build():
    _servers = ServersCommand(conf=conf)
    _servers.build()
    assert os.path.exists(conf['supervisor_conf'])
