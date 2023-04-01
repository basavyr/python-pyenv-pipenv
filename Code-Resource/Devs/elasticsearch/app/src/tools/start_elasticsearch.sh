#!/usr/bin/env sh

host=`uname -a | awk '{print $4}'`

if [ -z "$ES_HOME" ]; then
  echo "The path to Elasticsearch is not available"
else
  echo "Elasticsearch is configured at: $ES_HOME"
fi

echo "Starting Elasticsearch service on $host"
