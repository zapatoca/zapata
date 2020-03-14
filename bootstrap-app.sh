#!/usr/bin/env bash

GUEST_HOME=${GUEST_HOME:='.'}

export FLASK_APP=$GUEST_HOME/main.py
nohup python3 -m flask run --host=0.0.0.0 > /dev/null 2>&1 &
