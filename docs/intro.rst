.. Xonotic Server Management Suite Intro

Intro
=====

Xonotic Server Management Suite works with your existing workflow by generating configs for
and ochestrating popular management software such as the following, which are henceforth
referred to as `engines`:

    * `screen`_
    * `tmux`_
    * `supervisor`_
    * `docker`_

.. _screen: https://www.gnu.org/software/screen
.. _tmux: https://tmux.github.io
.. _supervisor: http://supervisord.org
.. _docker: https://www.docker.com

The configuration files are generated with a combination of `yml`, `conf` and `cfg` and provide
many opportunities for you to inject your existing assets and confings.

Lets start with a simple `servers.yml` to define a server that generates a server configuration
for a vanilla server, `vanilla.cfg`. This gets put in `~/.xonotic/data/server.pk3dir`, which to
DarkPlaces engine appears as `~/.xonotic/data`, so we can reference it simply as `vanilla.cfg`::

    # This file is read from ~/.xsms/servers.yml make sure that's where you are editing it
    version: '1'
    servers:
      vanilla:
        title: "-z- Simple vanilla"
        motd: "Welcome to ${hostname} | Owner: -z-"
        port: 26000
        maxplayers: 16
        net_address: ""
        exec: ./all run dedicated +serverconfig vanilla.cfg

The following command generates the `vanilla.cfg` file the `exec` line above references::

    xsms servers build

The contents of that generated file should look similar to::

    // Last Generated: 2016-10-30 19:39:17.026331
    hostname "-z- Simple vanilla"
    sv_motd "Welcome to ${hostname} | Owner: -z-"
    port 26000
    maxplayers 16
    net_address ""

Now you can start up the servers with your engine of choice, for example::

    xsms servers -e screen start

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
