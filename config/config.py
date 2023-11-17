# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


mod = "mod4"
terminal = "alacritty"
browser = "firefox"
rofi = "rofi -modes 'drun' -show drun"
font = "JetBrainsMono Nerd Font Mono"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.spawn(browser), desc="Launch Firefox"),  
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "Space", lazy.spawn(rofi), desc="Show a launcher"),
]

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["", "󰨞", "", "4", "5", "6", "7", "8", "9", "10"]
group_layouts = ["monadtall","monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"] 

for i in range(len(group_names)):
    groups.append(
            Group(
                name=group_names[i],
                layout=group_layouts[i].lower(),
                label=group_labels[i],
            ))

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Mod + Number to move to that group"),
        #Key([mod], "Tab", lazy.screen.next_group(), desc="Move to next group with tab"),
        #Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="Move to previous group with tab"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="Move focused window to new workspace"),
        ])

# ScratchPads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", f"{terminal} --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.8),
    DropDown("pavu", "pavucontrol", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.8),
    DropDown("ranger", f"{terminal} --class=ranger -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.8),
    ]))

keys.extend([
    Key([mod], "j", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([mod], "k", lazy.group["scratchpad"].dropdown_toggle("ranger")),

    ])

colors = dict(
    bg="#282a36",
    fg="#f8f8f2",
    light_gray="#44475a",
    blue="#6272a4",
    cyan="#8be9fd",
    green="#50fa7b",
    orange="#ffb86c",
    pink="#ff79c6",
    purple="#bd93f9",
    red="#ff5555",
    yellow="#f1fa8c",
)

layout_theme= {
        "margin": 30,
        "border_width": 2,
        "border_focus": colors["purple"],
        "border_normal": colors["light_gray"],
        }

layouts = [
        layout.MonadTall(**layout_theme),
        layout.Columns(**layout_theme),
        layout.Max(**layout_theme),
        ]

widget_defaults = dict(
    font=font,
    fontsize=12,
    padding=6,
    background=colors["bg"],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=colors["fg"],
                    background=colors["bg"],
                    fontsize=16,
                    highlight_method="line",
                    highlight_color=colors["light_gray"],
                    inactive=colors["light_gray"],
                    spacing=10,
                    this_current_screen_border=colors["orange"],
                    this_screen_border=colors["orange"],
                    urgent_alert_method="line",
                    urgent_border=colors["red"],
                    urgent_text=colors["red"],
                    hide_unused=True,
                ),
                widget.Sep(linewidth=1, padding=20, foreground=colors["bg"], background=colors["bg"]),
                widget.TaskList(
                    icon_size=27,
                    font=font,
                    foreground=colors["fg"],
                    background=colors["bg"],
                    borderwidth=0,
                    border=colors["bg"],
                    margin=0,
                    padding=0,
                    highlight_method="block",
                    title_width_method="uniform",
                    rounded=False,

                ),
                widget.Sep(linewidth=1, padding=20, foreground=colors["bg"], background=colors["bg"]),
                widget.TextBox(text="󰕾 ", fontsize=14, foreground=colors["fg"]),
                widget.PulseVolume(
                    foreground=colors["cyan"],
                    padding=10,
                ),
                widget.Sep(linewidth=1, padding=20, foreground=colors["bg"], background=colors["bg"]),
                widget.TextBox(text=" ", fontsize=14, foreground=colors["fg"]),
                widget.CPU(
                    update_interval=1.0,
                    format="{load_percent}%",
                    foreground=colors["yellow"],
                    padding=5,
                ),
                widget.Sep(linewidth=1, padding=20, foreground=colors["bg"], background=colors["bg"]),
                widget.TextBox(text="󰍛 ", fontsize=14, foreground=colors["fg"]),
                widget.Memory(
                    foreground=colors["orange"],
                    format="{MemUsed: .0f} / {MemTotal: .0f}{mm}",
                    measure_mem="G",
                    padding=5,
                ),
#                widget.Prompt(),
                widget.Sep(linewidth=1, padding=20, foreground=colors["bg"], background=colors["bg"]),
                widget.TextBox(text=" ", fontsize=14, foreground=colors["fg"]),
                widget.Clock(
                        format="%d.%m.%Y %a %H.%M %p",
                        padding=10,
                        foreground=colors["green"],
                ),
                widget.CurrentLayoutIcon(
                        scale=0.5,
                        foreground=colors["blue"],
                        background=colors["bg"],
                ),
            ],
            size=36,
            background=colors["bg"],
            margin=6,
            opacity=0.8
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
