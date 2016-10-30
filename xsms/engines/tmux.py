import libtmux
import subprocess


def start(servers, xonotic_root):
    """
    This engine enables programmatic control of tmux.

    :param servers:
    :param xonotic_root:

    .. note::
        This tries to create a new session with Popen() but it
        does not always work. It is therefore better to already
        have a tmux session running before using this command.

    >>> import yaml
    >>> from xsms.engines import tmux
    >>> from xsms.config import conf
    >>> with open(conf['servers_manifest']) as f:
    >>>     servers = yaml.load(f)
    >>> tmux.start(servers=servers, xonotic_root=conf['xonotic_root'])
    """
    server = libtmux.Server()
    p = subprocess.Popen(['tmux', 'new-session', '-s', 'xsms', '-n', 'main'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    session = server.find_where({"session_name": 'xsms'})

    for server in servers['servers']:
        print(server)
        session.new_window(attach=False, window_name=server, start_directory=xonotic_root, window_shell=servers['servers'][server]['exec'])
