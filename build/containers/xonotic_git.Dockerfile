FROM ubuntu:latest

# System Dependencies
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
   python3 \
   python3-pip \
   zip \
   unzip \
   curl \
   wget \
   git

# Xonotic
RUN git clone git://git.xonotic.org/xonotic/xonotic.git /opt/Xonotic && \
    cd /opt/Xonotic/ && \
    ./all update -l best && \
    ./all compile && \
    ./all compile dedicated

# SMB Configs
RUN mkdir -p ~/.xonotic/data && \
    touch ~/.xonotic/data/server.cfg && \
    git clone https://github.com/MarioSMB/smb-servers.git ~/.xonotic/data/smb-servers.pk3dir

# Xonotic Map Manager
RUN git clone https://github.com/z/xonotic-map-manager /opt/xmm && \
    cd /opt/xmm/ && \
    mkdir ~/.xmm && \
    pip3 install --upgrade pip && \
    python3 setup.py install

COPY containers/xonotic/xmm.cfg /root/.xmm.cfg
COPY containers/xonotic/xmm/servers.json /root/.xmm/servers.json

# Xonotic Server Management Suite
RUN git clone https://github.com/z/xonotic-server-management-suite /opt/xsms && \
    cd /opt/xsms/ && \
    python3 setup.py install

# These can be built into the image for deployment (put in build/ dir)
# COPY xsms.cfg /root/.xsms.cfg
# COPY servers.yml /root/.xsms/servers.yml


VOLUME ["~/.xonotic/data"]

WORKDIR /opt/Xonotic

CMD ["./all run dedicated"]

EXPOSE 26000
EXPOSE 26010
