#!/usr/bin/env sh
PID_FILE=elasticsearch.pid
LOCAL_DIR=`pwd`


if [ -s $PID_FILE ]; then
    PID=$(cat $PID_FILE)
    KILL_ES="kill -9 $PID"
    echo "Found an active Elasticsearch instance. Stopping it now..."
    eval $KILL_ES
    rm $PID_FILE
else
    echo "No active Elasticsearch instances"
fi