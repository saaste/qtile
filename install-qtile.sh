#!/usr/bin/bash

# Install Python PIP
sudo apt install python3-pip

# Install QTile
pip install xcffib
pip install qtile
pip install dbus-next
pip install psutil

# Background image manager
sudo apt install feh

# Terminal
sudo apt install gnome-terminal

# Rofi launcher
sudo apt install rofi

# Picom: compositor for X
sudo apt install picom

# Neovim
sudo apt install neovim

# Neofetch
sudo apt install neofetch

# Pavucontrol (audio)
sudo apt install pavucontrol

# Alacritty
sudo add-apt-repository ppa:aslatter/ppa -y
sudo apt install alacritty

# Needed by PulseAudio widget
pip install pulsectl-asyncio

# Ranger (file manager)
sudo apt install ranger
