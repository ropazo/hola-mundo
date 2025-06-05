#!/bin/bash
set -e
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
# install project requirements if we had any
pip install -r requirements.txt 2>/dev/null || true
