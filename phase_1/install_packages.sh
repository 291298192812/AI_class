#!/bin/bash


# go into the virtual enviroment
source .venv/bin/activate || exit
# start jupyter server
pip install --upgrade pip || exit
# install all needed or new packages
pip install jupyter numpy matplotlib pandas || exit
