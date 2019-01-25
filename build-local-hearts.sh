#!/bin/bash
#!/usr/bin/env python3

virtualenv -p python3.7 virtualenv

source virtualenv/bin/activate

echo "Installing python requirements"
pip install -r requirements.txt
