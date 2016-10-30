import screenutils


def start(servers, xonotic_root):
    """
    This engine enables programmatic control of screen.

    :param servers:
    :param xonotic_root:

    >>> import yaml
    >>> from xsms.engines import screen
    >>> from xsms.config import conf
    >>> with open(conf['servers_manifest']) as f:
    >>>     servers = yaml.load(f)
    >>> screen.start(servers=servers, xonotic_root=conf['xonotic_root'])
    """
    screen_sessions = {}

    for server in servers['servers']:
        screen_sessions[server] = screenutils.Screen(server, True)
        screen_sessions[server].send_commands('cd {0}'.format(xonotic_root))
        screen_sessions[server].send_commands(servers['servers'][server]['exec'])

    screenutils.list_screens()
