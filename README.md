# xonotic-server-management-suite

For managing infrastructure, tests, deployments of Xonotic game servers.

Current Features:

* Dockerized [Xonotic](http://xonotic.org) git and stable builds 
* [SMB configurations](https://github.com/MarioSMB/smb-servers) integrated
* [SMB Modpack](https://github.com/MarioSMB/modpack) support
* [Xonotic Map Manager](https://github.com/z/xonotic-map-manager) integration

## Requirements

* Python 3

#### With Docker

* docker
* docker-compose

#### Without Docker

Without Docker, you'll need to install Xonotic locally. Xonotic releases are available at [Xonotic.org](http://www.xonotic.org/download) and instructions for git are [available in the Xonotic wiki](https://gitlab.com/xonotic/xonotic/wikis/Repository_Access).

Use the Dockerfiles in `build/containers` for inspiration.

## Install

```
python setup.py install  # this clones the server configs and modpack
xsms smbmod init         # setup SMB modpack and assets
```

All custom server assets go in `~/.xonotic-smb` on the host which gets mounted
to `~/.xonotic` in the containers.

## XSMS Configuration

The defaults should work out of the box, if you want to make changes, edit the `~/.xsms.cfg` file.

```ini
[default]
xonotic_root = /opt/Xonotic
smb_init_script = bin/init.sh
smb_update_script = ~/.xonotic-smb/modpack/update.sh
smb_build_script = ~/.xonotic-smb/modpack/build.sh
smb_cache_path = ~/.xonotic-smb/modpack/.cache
data_csprogs = ~/.xonotic-smb/data_csprogs
servers = ~/.xsms/servers.yml
# Engines
supervisor_server_template = ~/.xsms/supervisor.server.conf.tpl
supervisor_conf = ~/.xsms/supervisor.conf
circus_server_template = ~/.xsms/circus.server.conf.tpl
circus_conf = ~/.xsms/circus.ini
```

### Defining Servers

*IN PROGRESS*

XSMS provides a YAML specification for defining the basic meta information for servers.

You can think of this as "xonotic-compose".

**Example:**

```yaml
version: '1'
servers:
  insta:
    title: "(SMB) Instagib+Hook USA"
    motd: |
      This is my long message of the day.
      It can be multiple lines.
    port: 26010
    exec: ./all run dedicated -game data_csprogs -game data_insta -sessionid insta +serverconfig configs/info-usainsta.cfg
  overkill:
    title: "(SMB) Overkill USA"
    motd: |
      This is my other long message of the day.
    port: 26004
    exec: ./all run dedicated -game data_csprogs -game data_overkill -sessionid overkill +serverconfig configs/info-overkill.cfg
```

## Usage

### With Docker

The easiest way to get started is with docker. The `docker-compose.yml` file contains containers for running either xonotic_git, xonotic_stable or both. 

```
docker-compose up              # this brings up the arch described in docker-compose.yml
# or
docker-compose up xonotic_git  # this brings up only the xonotic_git container 
docker-compose down            # this takes it down
```

#### Using XMM to manage maps

The link between XMM and servers is defined in `build/containers/xonotic/xmm/servers.json`.

In the example below, the server `insta` is used.

```
docker-compose exec xonotic_git /bin/bash  # connect to the docker container
xmm -s insta discover                      # finds any maps in this server's data dir
xmm -s insta install eggandscrambled.pk3   # install a new map
xmm -s insta list                          # list all maps tracked for this server
```

### Without Docker

Without docker, XSMS can manage game servers a few different ways using `xsms servers start` to start up your servers defined in `~/.xsms/servers.yml`. Supported (or planned) methods include: `screen, tmux` for interactive management and  `supervisor, circus` for daemon management. If you want simple map management, XMM Can be installed separately.

For daemons, conf files need to be generated with `xsms servers build`.
