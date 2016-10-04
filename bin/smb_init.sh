#!/bin/sh
mkdir -p ~/.xonotic-smb/data
# Grab SMB Configs
git clone https://github.com/MarioSMB/smb-servers.git ~/.xonotic-smb/data/smb-servers.pk3dir
# Grab SMB Modpack
git clone https://github.com/MarioSMB/modpack.git ~/.xonotic-smb/modpack
# Grab SMB Modpack assets
(cd ~/.xonotic-smb/data && curl https://raw.githubusercontent.com/MarioSMB/modpack/master/README.md | grep http://dl.xonotic.co | awk '{ print $2 }' | xargs -n1 curl -O)
# Build SMB Modpack
(cd ~/.xonotic-smb/modpack && ./update.sh && ./build.sh)
# Sync Assets to data_csprogs to trigger dl from file server
rsync -azvh ~/.xonotic-smb/modpack/.cache ~/.xonotic-smb/data_csprogs