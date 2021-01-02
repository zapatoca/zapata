#!/usr/bin/env bash

GUEST_HOME=${GUEST_HOME:='.'}

docker-compose -f $GUEST_HOME/docker-compose.yml up --build -d db app
