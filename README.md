# xonotic-server-manager

For managing infrastructure, tests, deployments of Xonotic game servers.

Current Features:

- Dockerized git and stable xonotic
- SMB configurations integrated
- SMB Modpack support

## Requirements

* docker
* docker-compose

## Install

```
./setup.sh          # this clones the server configs and modpack
docker-compose up   # this brings up the arch described in docker-compose.yml
```

All custom server assets go in `~/.xonotic-smb` on the host which gets mounted
to `~/.xonotic` in the containers.
