#!/bin/bash


# go into the virtual enviroment
source .venv/bin/activate || exit
# start jupyter server
jupyter notebook
