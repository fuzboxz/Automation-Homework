#!/bin/sh

# activate virtual environment
source bin/activate
# install pip dependencies
pip install -r requirements.txt
# authenticate to google
python Library/GoogAuth.py