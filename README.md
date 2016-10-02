# xonotic-server-management-suite

For managing infrastructure, tests, deployments of Xonotic game servers.

Current Features:

- Dockerized [Xonotic](http://xonotic.org) git and stable builds 
- [SMB configurations](https://github.com/MarioSMB/smb-servers) integrated
- [SMB Modpack](https://github.com/MarioSMB/modpack) support
- [Xonotic Map Manager](https://github.com/z/xonotic-map-manager) integration

## Requirements

* docker
* docker-compose

## Install

```
python setup.py install  # this clones the server configs and modpack
xsms smbmod init         # setup SMB modpack and assets
```

All custom server assets go in `~/.xonotic-smb` on the host which gets mounted
to `~/.xonotic` in the containers.

## Usage

```
docker-compose up    # this brings up the arch described in docker-compose.yml
docker-compose down  # this takes it down
```

###  Using XMM to manage maps

The link between XMM and servers is defined in `build/containers/xonotic/xmm/servers.json`.

In the example below, the server `insta` is used.

```
xmm -s insta discover                     # finds any maps in this server's data dir
xmm -s insta install eggandscrambled.pk3  # install a new map
xmm -s insta list                         # list all maps tracked for this server
```
