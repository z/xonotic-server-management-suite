.. Xonotic Server Management Suite documentation master file, created by
   sphinx-quickstart on Tue Oct  4 20:14:48 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Xonotic Server Management Suite's documentation!
===========================================================

For managing infrastructure, tests, deployments of Xonotic game servers.

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
   configuration
   usage
   engines
   xsms
   tests
   license


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
