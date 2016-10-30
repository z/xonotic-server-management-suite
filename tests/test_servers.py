import os
import xsms.util as util
from xsms.servers import ServersCommand
from xsms.config import conf

root_dir = os.path.dirname(os.path.abspath(__file__))


def test_generate_engine_configs():
    _servers = ServersCommand(conf=conf)
    _servers.generate_engine_configs()
    assert os.path.exists(conf['supervisor_conf'])


def test_generate_server_configs():
    _servers = ServersCommand(conf=conf)
    _servers.generate_server_configs()
    assert os.path.exists('{}/insta.cfg'.format(conf['xsms_servers_config_root']))


def test_generate_custom_server_configs():
    util.check_if_not_create('{}/servers/insta.cfg.tpl'.format(conf['xsms_servers_config_root']), '{}/data/servers/custom.cfg.tpl'.format(root_dir))
    _servers = ServersCommand(conf=conf)
    _servers.generate_server_configs()
    assert os.path.exists('{}/insta.cfg'.format(conf['xsms_servers_config_root']))