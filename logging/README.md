# docker logging

2 services (javascript & python) that, put out some log to stdout.

the current config logs all events to /var/log/syslog

put the following line in /etc/rsyslog.conf
`:syslogtag, contains, "logging_service"  /var/log/logging_service.log`

restart rsyslog
`sudo service rsyslog restart`

the messages are now also in a separate file
