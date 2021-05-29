#!/bin/sh

if [ -e venv/ ]; then
	echo "venv/ already exists"
else
	python3 -m venv venv/
	. venv/bin/activate
	pip3 install -r requirements.txt
fi
