.. Xonotic Server Management Suite Intro

Intro
=====

Game servers administration shouldn't be a full-time job, it should be enjoyable, like the game.
Great ideas should be tested, saved and reproducible.  Xonotic Server Management Suite works with
your existing workflow by *automating the boring stuff*.

Generate configurations for popular server management software tools, henceforth referred to as ``engines``,
through a normalized ``YAML`` format without compromise:

* `screen`_
* `tmux`_
* `supervisor`_
* `docker`_

Optionally, use the built in ``xsms``, and ``xmm`` tools to manage your servers and their ``engines``.

.. _screen: https://www.gnu.org/software/screen
.. _tmux: https://tmux.github.io
.. _supervisor: http://supervisord.org
.. _docker: https://www.docker.com

The configuration files are generated with a combination of ``yml``, ``conf`` and ``cfg`` and provide
many opportunities to inject existing assets and configurations for any supported ``engine``.

Start with a simple ``servers.yml`` to define a single server that generates a server configuration for
a vanilla server, ``vanilla.cfg``. This gets put in ``~/.xonotic/data/server.pk3dir``, which to the
DarkPlaces engine appears as ``~/.xonotic/data``, making it avaiable to reference as ``vanilla.cfg``::

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

The following command will generate the ``vanilla.cfg`` file the ``exec`` line above references::

    xsms servers build

The contents of that generated file will look similar to::

    // Last Generated: 2016-10-30 19:39:17.026331
    hostname "-z- Simple vanilla"
    sv_motd "Welcome to ${hostname} | Owner: -z-"
    port 26000
    maxplayers 16
    net_address ""

Start up the servers with your ``engine`` of choice, for example::

    xsms servers -e screen start
.

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
