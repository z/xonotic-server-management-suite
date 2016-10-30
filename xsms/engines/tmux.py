import libtmux
import subprocess


def start(servers, xonotic_root):
    server = libtmux.Server()
    p = subprocess.Popen(['tmux', 'new-session', '-s', 'xsms', '-n', 'main'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    session = server.find_where({"session_name": 'xsms'})

    for server in servers['servers']:
        print(server)
        session.new_window(attach=False, window_name=server, start_directory=xonotic_root, window_shell=servers['servers'][server]['exec'])
