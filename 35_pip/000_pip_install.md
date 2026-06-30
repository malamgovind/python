# ============================================
# PIP COMMANDS (Ubuntu)
# ============================================

# Python Version Check
python3 --version

# pip Version Check
pip --version

# pip3 Version Check
pip3 --version

# જો pip Install ન હોય તો
sudo apt update
sudo apt install python3-pip

# ફરી Version Check
pip3 --version

# pip Upgrade
python3 -m pip install --upgrade pip

# ============================================
# Virtual Environment (venv)
# ============================================

# venv Package Install
sudo apt install python3-venv

# Project Folder માં જાઓ
cd ~/Documents/python-learning

# Virtual Environment બનાવો
python3 -m venv venv

# Virtual Environment Activate કરો
source venv/bin/activate

# Prompt આવું દેખાશે
(venv) hari@ubuntu:~/Documents/python-learning$

# Installed Packages જુઓ
pip list

# Package Install કરો
pip install requests

# Multiple Packages Install
pip install requests numpy pandas

# Package Information
pip show requests

# Package Upgrade
pip install --upgrade requests

# Package Uninstall
pip uninstall requests

# Requirements File બનાવો
pip freeze > requirements.txt

# Requirements File થી Packages Install
pip install -r requirements.txt

# Virtual Environment Deactivate
deactivate

# ============================================
# Useful Commands
# ============================================

# બધા Installed Packages
pip list

# Outdated Packages
pip list --outdated

# Package Search (જૂના pip માં કામ કરતું હતું, હવે Remove થયું છે)
# pip search requests

# pip Help
pip --help