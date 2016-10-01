FROM ubuntu:latest

RUN \
  apt-get update && \
  apt-get install -y build-essential \
   xserver-xorg-dev \
   x11proto-xf86dri-dev \
   x11proto-xf86dga-dev \
   x11proto-xf86vidmode-dev \
   libxxf86dga-dev \
   libxcb-xf86dri0-dev \
   libxpm-dev \
   libxxf86vm-dev \
   libsdl1.2-dev \
   libsdl2-dev \
   libsdl2-image-dev \
   libclalsadrv-dev \
   libasound2-dev \
   libxext-dev \
   libjpeg-turbo8-dev \
   zlib1g-dev \
   zip \
   unzip \
   curl \
   wget \
   git

RUN git clone git://git.xonotic.org/xonotic/xonotic.git /opt/Xonotic && \
    cd /opt/Xonotic/ && \
    ./all update -l best && \
    ./all compile dedicated

RUN mkdir -p ~/.xonotic/data && \
    touch ~/.xonotic/data/server.cfg && \
    git clone https://github.com/MarioSMB/smb-servers.git ~/.xonotic/data/smb-servers.pk3dir

VOLUME ["~/.xonotic/data"]

WORKDIR /opt/Xonotic

CMD ["./all run dedicated"]

EXPOSE 26000
EXPOSE 26010
