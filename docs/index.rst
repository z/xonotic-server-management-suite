.. Xonotic Server Management Suite documentation master file, created by
   sphinx-quickstart on Tue Oct  4 20:14:48 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Xonotic Server Management Suite's documentation!
===========================================================

Xonotic Server Management Suite is a collection of tools and best practices for
managing infrastructure, tests, and deployments of Xonotic game servers.

.. code-block:: yaml

    version: '1'
    servers:
      vanilla:
        title: "-z- Simple vanilla"
        motd: "Welcome to ${hostname} | Owner: -z-"
        port: 26000
        maxplayers: 16
        net_address: ""
        use_smbmod: false
        exec: ./all run dedicated +serverconfig vanilla.cfg
      insta:
        title: "(SMB) Instagib+Hook USA"
        motd: "Welcome to ${hostname} | Owner: AllieWay | Admins: Mario, muffin, -z- | Hello from xsms"
        port: 26010
        maxplayers: 64
        net_address: ""
        use_smbmod: true
        exec: ./all run dedicated -game modpack -game data_csprogs -game data_insta -sessionid insta +serverconfig insta.cfg


.. image:: https://travis-ci.org/z/xonotic-server-management-suite.svg?branch=develop
    :target: https://travis-ci.org/z/xonotic-server-management-suite

**Features**

* Dockerized `Xonotic`_ git and stable builds
* `SMB configurations`_ integrated
* `SMB Modpack`_ support
* `Xonotic Map Manager`_ integration
* Define your servers in `YAML` or `cfg`
* Works with your existing workflow using:
    * `screen`_
    * `tmux`_
    * `supervisor`_
    * `docker`_


.. _Xonotic: http://xonotic.org
.. _SMB Modpack: https://github.com/MarioSMB/smb-servers
.. _SMB configurations: https://github.com/MarioSMB/smb-servers
.. _Xonotic Map Manager: https://github.com/z/xonotic-map-manager
.. _screen: https://www.gnu.org/software/screen
.. _tmux: https://tmux.github.io
.. _supervisor: http://supervisord.org
.. _docker: https://www.docker.com

**Get Started**

.. toctree::
   :maxdepth: 2

   intro
   installation
   configuration
   usage
   api
   tests
   license


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
