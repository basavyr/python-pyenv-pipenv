#!/usr/bin/env sh

#config vars
MACOSOS=Darwin
MB_AIR="Roberts-MacBook-Air.local"
LOCAL_DIR=`pwd`

# takes the OS version of the current platform on which the script is running
HOST=`uname -a | awk '{print $4}'`

if [ "$HOST" == $MACOSOS ] || [ "$HOST" == "Darwin" ] || [ "$HOST" == "macOS" ]; then
  echo "The current platform is MacOS"
  ELK_MODE="cd $ES_HOME && ./bin/elasticsearch -d -p $LOCAL_DIR/elasticsearch.pid > $LOCAL_DIR/elasticsearch.log 2>&1``"
else
  echo "The current platform is Linux based"
  ELK_MODE="systemctl status elasticsearch"
fi

if [ -z "$ES_HOME" ] && [ -z "$KIBANA_HOME" ] ; then
  echo "The path to Elasticsearch and Kibana are not available"
else
  echo "Elasticsearch is configured at: $ES_HOME"
  echo "Kibana is configured at: $KIBANA_HOME"
  echo "Saving data in $LOCAL_DIR"
  eval $ELK_MODE
fi
