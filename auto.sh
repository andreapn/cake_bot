#!/bin/bash

PYTHON_PATH=/usr/local/bin/python3.9
pipenv --python $PYTHON_PATH
cd /home/ec2-user/cake_bot/ || exit
pipenv install
pipenv run python -u ./auto_sell.py > ./output.log