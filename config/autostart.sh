#!/usr/bin/bash

# Set resolution
xrandr --newmode "2560x1440_60.00"  311.83  2560 2744 3024 3488  1440 1441 1444 1490  -HSync +Vsync
xrandr --addmode Virtual1 "2560x1440_60.00"
xrandr --output Virtual1 --primary --mode "2560x1440_60.00" --pos 0x0 --rotate normal

# Set background
feh --bg-scale ~/Pictures/wallpapers/retro.jpg & nm-applet &

picom --experimental-backends -b &
