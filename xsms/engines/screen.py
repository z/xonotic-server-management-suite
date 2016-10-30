import screenutils


def start(servers, xonotic_root):
    screen_sessions = {}

    for server in servers['servers']:
        screen_sessions[server] = screenutils.Screen(server, True)
        screen_sessions[server].send_commands('cd {0}'.format(xonotic_root))
        screen_sessions[server].send_commands(servers['servers'][server]['exec'])

    screenutils.list_screens()
