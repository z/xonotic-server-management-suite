FROM debian:latest

ENV XONOTIC_DOWNLOAD_URL=http://dl.xonotic.org/xonotic-0.8.1.zip

RUN \
  apt-get update && \
  apt-get install -y zip unzip curl wget git

RUN wget $XONOTIC_DOWNLOAD_URL -q --progress=bar -O /opt/xonotic.zip && \
    unzip /opt/xonotic.zip -d /opt && \
    rm /opt/xonotic.zip && \
    cp /opt/Xonotic/server/server_linux.sh /opt/Xonotic/server_linux.sh

RUN mkdir -p ~/.xonotic/data && \
    touch ~/.xonotic/data/server.cfg && \
    git clone https://github.com/MarioSMB/smb-servers.git ~/.xonotic/data/smb-servers.pk3dir

WORKDIR /opt/Xonotic

CMD ["/opt/Xonotic/server_linux.sh"]

EXPOSE 26000
EXPOSE 26010
