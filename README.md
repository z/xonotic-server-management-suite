# xonotic-server-management-suite

For managing infrastructure, tests, deployments of Xonotic game servers.

[![Build Status](https://travis-ci.org/z/xonotic-server-management-suite.svg?branch=develop)](https://travis-ci.org/z/xonotic-server-management-suite) [![Documentation Status](https://readthedocs.org/projects/xonotic-server-management-suite/badge/?version=latest)](http://xonotic-server-management-suite.readthedocs.io/en/latest/?badge=latest)


**Features**:

* Dockerized [Xonotic](http://xonotic.org) git and stable builds
* [SMB configurations](https://github.com/MarioSMB/smb-servers) integrated
* [SMB Modpack](https://github.com/MarioSMB/modpack) support
* [Xonotic Map Manager](https://github.com/z/xonotic-map-manager) integration
* Define your servers in `YAML` or `cfg`
* Works with your existing workflow using:
    * [screen](https://www.gnu.org/software/screen/)
    * [tmux](https://tmux.github.io/)
    * [supervisor](http://supervisord.org/)

**Define Your servers**:

```yaml
# This file is read from ~/.xsms/servers.yml make sure that's where you are editing it
version: '1'
servers:
  insta:
    title: "(SMB) -z- Simple Insta"
    motd: "Welcome to ${hostname} | Owner: -z-"
    port: 26000
    maxplayers: 16
    net_address: ""
    exec: ./all run dedicated +serverconfig insta.cfg
```

**Build and Run**:

```
xsms servers build
xsms servers start -e screen
```

## Requirements

* Python 3
* A supported engine (screen, tmux, supervisor)

#### With Docker

* docker
* docker-compose

#### Without Docker

* Local installation of Xonotic:
    * Xonotic releases are available at [Xonotic.org](http://www.xonotic.org/download)
    * Instructions for git are [available in the Xonotic wiki](https://gitlab.com/xonotic/xonotic/wikis/Repository_Access)

instructions for git are [available in the Xonotic wiki](https://gitlab.com/xonotic/xonotic/wikis/Repository_Access)

Use the Dockerfiles in `docker/containers` for inspiration.

## Install

```
python setup.py install  # this clones the server configs and modpack
xsms smbmod init         # setup SMB modpack and assets (optional)
```

All custom server assets go in `~/.xonotic-smb` on the host which gets mounted
to `~/.xonotic` in the containers.

## Documentation

Documentation is hosted on [readthedocs.io](http://xonotic-server-management-suite.readthedocs.io/en/latest).

## License

Copyright (c) 2016 Tyler Mulligan (z@xnz.me) and contributors.

Distributed under the MIT license. See the LICENSE file for more details.