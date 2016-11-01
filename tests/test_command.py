import os
import xsms.util as util
from xsms.command import Command
from xsms.config import conf

root_dir = os.path.dirname(os.path.abspath(__file__))


def test_command_object():
    command = Command(conf=conf)
    assert isinstance(command, Command)
    assert command.conf['xsms_config_root'] == os.path.expanduser('~/.xsms')


def test_command_generate_engine_configs():
    command = Command(conf=conf)
    command.generate_engine_configs()
    assert os.path.exists(conf['supervisor_conf'])


def test_command_generate_server_configs():
    command = Command(conf=conf)
    command.generate_server_configs()
    assert os.path.exists('{}/insta.cfg'.format(conf['xsms_generated_servers_root']))


def test_command_generate_custom_server_configs():
    util.check_if_not_create('{}/insta.cfg.tpl'.format(conf['xsms_templates_servers_root']), '{}/data/servers/custom.cfg.tpl'.format(root_dir))
    command = Command(conf=conf)
    command.generate_server_configs()
    assert os.path.exists('{}/insta.cfg'.format(conf['xsms_generated_servers_root']))