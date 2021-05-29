#!/bin/sh

if [ ! -e secret.key ]; then
	echo "Generating secret.key";
	head -c 32 /dev/urandom | xxd -p > secret.key
fi

FLASK_APP=app.py flask run
