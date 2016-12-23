FROM detrate/xonotic-docker:git
MAINTAINER Tyler Mulligan <z@xnz.me>

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

COPY containers/xsms/xmm.ini ~/.xmm.ini
COPY containers/xsms/xmm.logging.ini ~/.xmm.logging.ini
COPY containers/xsms/xmm/servers.json ~/.xmm/servers.json
COPY containers/xsms/xmm/sources.json ~/.xmm/sources.json

# Xonotic Server Management Suite
RUN git clone https://github.com/z/xonotic-server-management-suite /opt/xsms && \
    cd /opt/xsms/ && \
    python3 setup.py install

# Engines
RUN systemctl enable supervisor && \
    touch /var/run/supervisor.sock && \
    chmod 777 /var/run/supervisor.sock && \
    service supervisor restart

# These can be built into the image for deployment (put in docker/ dir)
# COPY xsms.cfg ~/.xsms.cfg
# COPY servers.yml ~/.xsms/servers.yml

WORKDIR /opt/Xonotic

CMD ["./all run dedicated"]
