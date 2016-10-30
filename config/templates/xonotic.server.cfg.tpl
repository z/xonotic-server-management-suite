// Compacted server configuration for SMB Insta

exec configs/auth-smb.cfg
exec configs/common-smb.cfg
exec configs/aliases-{servername}.cfg
exec configs/server-{servername}.cfg

hostname "{title}"
sv_motd "{motd}"
port {port}
maxplayers {maxplayers}
net_address "{net_address}"