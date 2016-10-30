import xsms.util as util
import os

config_file = '.xsms.cfg'
home = os.path.expanduser('~')
config_file_with_path = os.path.join(home, config_file)

util.check_if_not_create(config_file_with_path, 'config/xsms.cfg')

config = util.parse_config(config_file_with_path)

conf = {
    'xsms_config_root': os.path.expanduser('~/.xsms'),
    'xsms_servers_config_root': os.path.expanduser('~/.xsms/servers'),
    'xonotic_root': os.path.expanduser(config['xonotic_root']),
    'smb_init_script': os.path.expanduser(config['smb_init_script']),
    'smb_update_script': os.path.expanduser(config['smb_update_script']),
    'smb_build_script': os.path.expanduser(config['smb_build_script']),
    'smb_cache_path': os.path.expanduser(config['smb_cache_path']),
    'data_csprogs': os.path.expanduser(config['data_csprogs']),
    'servers_manifest': os.path.expanduser(config['servers']),
    'xonotic_server_template': os.path.expanduser(config['xonotic_server_template']),
    'supervisor_server_template': os.path.expanduser(config['supervisor_server_template']),
    'supervisor_conf': os.path.expanduser(config['supervisor_conf']),
}

# Setup templates in ~/.xsms
util.check_if_not_create(conf['servers_manifest'], 'config/servers.yml')
util.check_if_not_create(conf['xonotic_server_template'], 'config/xonotic.server.cfg.tpl')
util.check_if_not_create(conf['supervisor_server_template'], 'config/supervisor.server.conf.tpl')

# Make sure needed dirs exist
os.makedirs(conf['xsms_servers_config_root'], exist_ok=True)
