#!/bin/bash

# NB: This script was tested for Ubuntu 20.04 LTS which is shipped with Python 3 and snap

# clone repository in the directory of your choice
# install git if needed
# sudo apt install -y git
# cd {BASE_FOLDER}
# git clone git@github.com:mihersch/moyensDOinfVD.git

# update the system
sudo apt update
sudo apt -y upgrade

# install VC code
sudo snap install --classic code

# install VS Code extensions
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension redhat.vscode-yaml
code --install-extension executablebookproject.myst-highlight
code --install-extension seunlanlege.action-buttons
code --install-extension ban.spellright

# install virtual environment and Python dependencies
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt
