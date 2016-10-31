Configuration
=============

The defaults should work out of the box, if you want to make changes, edit the ``~/.xsms.cfg`` file.::

    [default]
    # Xonotic
    xonotic_root = /opt/Xonotic
    xonotic_userdir = ~/.xonotic
    xonotic_server_pk3dir = ~/.xonotic/servers.pk3dir
    servers = ~/.xsms/servers.yml
    xonotic_server_template = ~/.xsms/templates/xonotic.server.cfg.tpl
    xonotic_smbmod_server_template = ~/.xsms/templates/xonotic.smbmod-server.cfg.tpl

    # Engines
    supervisor_server_template = ~/.xsms/templates/supervisor.server.conf.tpl
    supervisor_conf_template = ~/.xsms/templates/supervisor.conf.tpl
    supervisor_conf = ~/.xsms/generated/supervisor.conf

    # SMB
    smb_init_script = bin/smb_init.sh
    smb_update_script = ~/.xonotic-smb/modpack/update.sh
    smb_build_script = ~/.xonotic-smb/modpack/build.sh
    smb_cache_path = ~/.xonotic-smb/modpack/.cache
    data_csprogs = ~/.xonotic-smb/data_csprogs

Defining Servers
----------------

XSMS provides a ``YAML`` specification for defining the basic meta information for servers.

You can think of this as *xonotic-compose*.

**Example:**::

    # This file is read from ~/.xsms/servers.yml make sure that's where you are editing it
    version: '1'
    servers:
      insta:
        title: "(SMB) Instagib+Hook USA"
        motd: "Welcome to ${hostname} | Owner: AllieWay | Admins: Mario, muffin, -z- | Hello from xsms"
        port: 26010
        maxplayers: 64
        net_address: ""
        use_smbmod: true
        exec: ./all run dedicated -game modpack -game data_csprogs -game data_insta -sessionid insta +serverconfig insta.cfg
      overkill:
        title: "(SMB) Overkill USA"
        motd: |
          This is my long message of the day.
          On multiple lines
        port: 26004
        maxplayers: 32
        net_address: ""
        use_smbmod: true
        exec: ./all run dedicated -game modpack -game data_csprogs -game data_overkill -sessionid overkill +serverconfig configs/info-overkill.cfg


This YAML file will generate a xonotic-compatible ``.cfg`` in ``~/.xsms/generated/servers/``.

Custom Server Configuration
---------------------------

Custom server templates are defined in ``~/.xsms/templates/servers/<servername>.cfg.tpl`` where ``<servername>`` corresponds with the name of the server defined in the YAML. See the ``tests`` folder for an example.


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
