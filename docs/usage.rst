Usage
=====

With Docker
-----------

The easiest way to get started is with docker. The `docker-compose.yml` file contains containers for running either xonotic_git, xonotic_stable or both.::

    docker-compose up              # this brings up the arch described in docker-compose.yml
    # or
    docker-compose up xonotic_git  # this brings up only the xonotic_git container
    docker-compose down            # this takes it down


Using XMM to manage maps
~~~~~~~~~~~~~~~~~~~~~~~~

The link between XMM and servers is defined in `docker/containers/xonotic/xmm/servers.json`.

In the example below, the server `insta` is used.::

    docker-compose exec xonotic_git /bin/bash  # connect to the docker container
    xmm update                                 # get the latest package list
    xmm -s insta discover                      # finds any maps in this server's data dir
    xmm -s insta install eggandscrambled.pk3   # install a new map
    xmm -s insta list                          # list all maps tracked for this server


Without Docker
--------------

Without docker, XSMS can manage game servers a few different ways using `xsms servers start` to start up your servers defined in `~/.xsms/servers.yml`. Supported (or planned) methods include: `screen, tmux` for interactive management and `supervisor, circus` for daemon management. If you want simple map management, XMM Can be installed separately.

For daemons, conf files need to be generated with `xsms servers build`.


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
