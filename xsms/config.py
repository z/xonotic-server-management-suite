import xsms.util as util
import os

config_file = '.xsms.cfg'
home = os.path.expanduser('~')
config_file_with_path = os.path.join(home, config_file)

util.check_if_not_create(config_file_with_path, 'config/xsms.cfg')

config = util.parse_config(config_file_with_path)

# Init configuration object
conf = {
    'xsms_config_root': os.path.expanduser('~/.xsms'),
    'xsms_templates_root': os.path.expanduser('~/.xsms/templates'),
    'xsms_templates_servers_root': os.path.expanduser('~/.xsms/templates/servers'),
    'xsms_generated_root': os.path.expanduser('~/.xsms/generated'),
    'xsms_generated_servers_root': os.path.expanduser('~/.xsms/generated/servers'),
    'xonotic_root': os.path.expanduser(config['xonotic_root']),
    'xonotic_userdir': os.path.expanduser(config['xonotic_userdir']),
    'xonotic_server_pk3dir': os.path.expanduser(config['xonotic_server_pk3dir']),
    'smb_init_script': os.path.expanduser(config['smb_init_script']),
    'smb_update_script': os.path.expanduser(config['smb_update_script']),
    'smb_build_script': os.path.expanduser(config['smb_build_script']),
    'smb_cache_path': os.path.expanduser(config['smb_cache_path']),
    'data_csprogs': os.path.expanduser(config['data_csprogs']),
    'servers_manifest': os.path.expanduser(config['servers']),
    'xonotic_server_template': os.path.expanduser(config['xonotic_server_template']),
    'xonotic_smbmod_server_template': os.path.expanduser(config['xonotic_smbmod_server_template']),
    'supervisor_conf_template': os.path.expanduser(config['supervisor_conf_template']),
    'supervisor_server_template': os.path.expanduser(config['supervisor_server_template']),
    'supervisor_conf': os.path.expanduser(config['supervisor_conf']),
}

# Add templates to ~/.xsms/templates/
util.check_if_not_create(conf['servers_manifest'], 'config/servers.yml')
util.check_if_not_create(conf['xonotic_server_template'], 'config/templates/xonotic.server.cfg.tpl')
util.check_if_not_create(conf['xonotic_smbmod_server_template'], 'config/templates/xonotic.smbmod-server.cfg.tpl')
util.check_if_not_create(conf['supervisor_conf_template'], 'config/templates/supervisor.conf.tpl')
util.check_if_not_create(conf['supervisor_server_template'], 'config/templates/supervisor.server.conf.tpl')

# Make sure needed dirs exist
os.makedirs(conf['xsms_templates_servers_root'], exist_ok=True)
os.makedirs(conf['xsms_generated_servers_root'], exist_ok=True)
os.makedirs(conf['xonotic_userdir'], exist_ok=True)

# Setup symlinks
if not os.path.exists(conf['xonotic_server_pk3dir']):
    os.symlink(conf['xsms_generated_servers_root'], conf['xonotic_server_pk3dir'])
