Installation
============

Requirements
------------

* Python 3
* A supported engine (screen, tmux, supervisor)

With Docker
~~~~~~~~~~~

* docker
* docker-compose

Without Docker
~~~~~~~~~~~~~~

* Local installation of Xonotic:
    * `Xonotic releases`_ are available at Xonotic.org
    * Instructions for git are `available in the Xonotic wiki`_

.. _Xonotic releases: http://xonotic.org/download
.. _available in the Xonotic wiki: https://gitlab.com/xonotic/xonotic/wikis/Repository_Access

Use the Dockerfiles in ``docker/containers`` for inspiration.

Install
-------

Install with setuptools::

   python3 setup.py install  # this clones the server configs and modpack
   xsms smbmod init          # setup SMB modpack and assets (optional)

If using docker, all custom server assets go in `~/.xonotic-smb` on the host
which gets mounted to `~/.xonotic` in the containers.

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`