#!/bin/sh
# chkconfig: - 95 95
### BEGIN INIT INFO
# Provides:          someservice
# Required-Start:    $ALL
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:
# X-Interactive:     false
# Short-Description: someservice
# Description:       someservice
### END INIT INFO


# this service is meant to start and stop crm


DESC="someservice"
NAME=web.py
PROCESS='web.py'
RUNCOMMAND="./web.py"
HOME='/var/local/someservice/'
LOGFILE='/tmp/log.log'

do_start()
{
    echo "$NAME starting ... ";
    cd $HOME
    nohup $RUNCOMMAND >/dev/null 2>&1 &
    sleep 1
    get_status
}

do_stop()
{
    echo "$NAME stopping ... ";
    killall $NAME
    ps aux | grep $PROCESS | grep -v 'grep' | awk '{print $2}' | xargs kill
    sleep 1
    get_status
}

do_restart()
{
    do_stop
    sleep 2
    do_start
}

do_show_log()
{
    tail -n100 -f $LOGFILE
}

get_status()
{
    ps_out=$(ps aux | grep $PROCESS | grep -v 'grep')
    if [ -n "$ps_out" ]; then
        pid=$(ps x | grep $PROCESS | grep -v 'grep' | awk '{ print $1 }')
        echo " * $NAME is start/running, process $pid"
    else
        echo " * $NAME is not running"
    fi
}

case "$1" in
    start)
    do_start
    ;;
    stop)
    do_stop
    ;;
    kill)
    do_stop
    ;;
    restart)
    do_restart
    ;;
    status)
    get_status
    ;;
    log)
    do_show_log
    ;;
    -h) echo "Valid arguments are: start, stop/kill, restat, status, log"
    ;;
    *) echo "Command $1 won't be processed, valid commands are: start, stop/kill, restat, status, log"
    ;;
esac

exit 0