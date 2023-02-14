#! /bin/bash

cd ~/notificador_site
git pull
source venv/bin/activate
pip install -r requirements.txt
python main.py
