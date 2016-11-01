from xsms.engines.screen import Session as screen
from xsms.engines.tmux import Session as tmux
from xsms.engines.supervisor import Session as supervisor
from xsms.server import Servers
from xsms.server import Server
from xsms.config import conf


def test_engines_screen_object():
    session = screen(conf=conf)
    servers = session.read_servers_manifest(filename=conf['servers_manifest'])
    assert isinstance(session, screen)
    assert not isinstance(session, tmux)
    assert isinstance(servers, Servers)
    assert isinstance(servers.servers[0], Server)


def test_engines_tmux_object():
    session = tmux(conf=conf)
    servers = session.read_servers_manifest(filename=conf['servers_manifest'])
    assert isinstance(session, tmux)
    assert not isinstance(session, screen)
    assert isinstance(servers, Servers)
    assert isinstance(servers.servers[0], Server)


def test_engines_supervisor_object():
    session = supervisor(conf=conf)
    servers = session.read_servers_manifest(filename=conf['servers_manifest'])
    assert isinstance(session, supervisor)
    assert not isinstance(session, screen)
