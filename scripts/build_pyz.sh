#!/bin/bash

########################
## Build pyz application
########################

APP_NAME=$(grep "APP_NAME = '" changeln/src/support/conf.py  | sed "s/ //g" | sed "s/'//g" | sed "s/APP_NAME=//g")
APP_VERSION=$(grep "APP_VERSION = '" changeln/src/support/conf.py  | sed "s/ //g" | sed "s/'//g" | sed "s/APP_VERSION=//g")

# Clean old build
rm -r dist build ./*.egg-info

# Dependency
pip install . --target dist

# Build pyz
shiv --site-packages dist --compressed -p '.venv python' -o "builds/$APP_NAME-$APP_VERSION.pyz" -e changeln.__main__:main

# Clean after build
rm -r dist build ./*.egg-info
