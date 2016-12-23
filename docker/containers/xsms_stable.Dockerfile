FROM detrate/xonotic-docker:stable
MAINTAINER Tyler Mulligan <z@xnz.me>

ENV XONOTIC_DOWNLOAD_URL=http://dl.xonotic.org/xonotic-0.8.1.zip

RUN mkdir -p ~/.xonotic/data && \
    touch ~/.xonotic/data/server.cfg && \
    git clone https://github.com/MarioSMB/smb-servers.git ~/.xonotic/data/smb-servers.pk3dir

WORKDIR /opt/Xonotic

CMD ["/opt/Xonotic/server_linux.sh"]
