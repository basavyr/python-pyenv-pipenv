#!/usr/bin/env sh
pid=$(cat elasticsearch.pid)
kill -15 $pid
