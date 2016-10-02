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
python setup.py install  # this clones the server configs and modpack
xsms smbmod init         # setup SMB modpack and assets 
docker-compose up        # this brings up the arch described in docker-compose.yml
```

All custom server assets go in `~/.xonotic-smb` on the host which gets mounted
to `~/.xonotic` in the containers.
