#!/bin/bash


# show errors
set -euo pipefail

# install the arch linux packages (assume it's installed)
# sudo pacman -S python
# create the virtual enviroment
python -m venv .venv || exit
# activate enviroment
source .venv/bin/activate || exit
# make sure pip is updated
pip install --upgrade pip || exit
# install jupyter notebook and other librarues
pip install jupyter numpy matplotlib pandas || exit

# lunch with jupyter notebook and visit
# the link using a browser
