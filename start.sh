#!/bin/bash

virtualenv --python=python3.6 venv

source venv/bin/activate

pip install -r requirements.txt

python main.py