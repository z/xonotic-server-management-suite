[supervisord]
nodaemon=true

[unix_http_server]
file = /var/run/supervisor.sock
chmod = 0777

[supervisorctl]
serverurl = unix:///var/run/supervisord.sock

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface