#     _                                        
# ___| |_ _   _ _ __ _ __ ___   __ _ _ __  ___ 
#/ __| __| | | | '__| '_ ` _ \ / _` | '_ \/ __|
#\__ \ |_| |_| | |  | | | | | | (_| | | | \__ \
#|___/\__|\__, |_|  |_| |_| |_|\__,_|_| |_|___/
#         |___/                                
#  ___  _   _ _                             __ _       
# / _ \| |_(_) | ___        ___ ___  _ __  / _(_) __ _ 
#| | | | __| | |/ _ \_____ / __/ _ \| '_ \| |_| |/ _` |
#| |_| | |_| | |  __/_____| (_| (_) | | | |  _| | (_| |
# \__\_\\__|_|_|\___|      \___\___/|_| |_|_| |_|\__, |


import os, re, shutil, socket, subprocess
from libqtile import bar, hook, layout, qtile 
from libqtile.config import EzClick as Click, EzDrag as Drag, Group, EzKey as Key, Match, Rule, Screen
from libqtile.lazy import lazy
from typing import List  # noqa: F401
from libqtile.widget import Spacer
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.bar import Bar
from qtile_extras.widget import modify


home = os.path.expanduser('~')
terminal = "kitty"
myBrowser = "librewolf"

keys = [
    # Switch between windows
    Key("M-h", lazy.layout.left(), desc="Move focus to left"),
    Key("M-l", lazy.layout.right(), desc="Move focus to right"),
    Key("M-j", lazy.layout.down(), desc="Move focus down"),
    Key("M-k", lazy.layout.up(), desc="Move focus up"),
    Key("M-<space>", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key("M-S-h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key("M-S-l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key("M-S-j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key("M-S-k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key("M-C-h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key("M-C-l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key("M-C-j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key("M-C-k", lazy.layout.grow_up(), desc="Grow window up"),
    Key("M-n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
   # Key("M-S-<Return>", lazy.layout.toggle_split(),
   #     desc="Toggle between split and unsplit sides of stack"),
    Key("M-<Return>", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key("M-<Tab>", lazy.next_layout(), desc="Toggle between layouts"),
    Key("M-q", lazy.window.kill(), desc="Kill focused window"),

    Key("M-C-r", lazy.restart(), desc="Restart Qtile"),
    Key("M-C-q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key("M-r", lazy.spawncmd(), 
desc="Spawn a command using a prompt widget"),
    # keybindigs to launch my scripts
    Key("M-S-x", lazy.spawn("/home/styrman/.scripts/power.sh"), desc="Run a power scripts"),
    Key("M-c", lazy.spawn("/home/styrman/.scripts/dmenu-configs.sh"), desc="Run my config-scripts"),
    Key("M-S-b", lazy.spawn("/home/styrman/.scripts/backup.sh"), desc="Run Backup"),

    # Keybindings to launch user defined programs
    Key("M-S-<Return>", lazy.spawn("dmenu_run"), desc="Launch dmenu"),
    Key("A-e", lazy.spawn("emacs"), desc="Launch emacs"),
    Key("M-f", lazy.spawn("thunar"), desc="Launch pcmanfm"),
    Key("A-m", lazy.spawn("/usr/local/src/thunderbird/thunderbird"), desc="Launch thunderbird"),
    Key("M-n", lazy.spawn("nitrogen"), desc="Launch nitrogen"),
    Key("A-r", lazy.spawn("rofi -show run"), desc="Launch rofi"),
    Key("A-s", lazy.spawn("st"), desc="Launch suckless terminal"),
    Key("A-t", lazy.spawn("urxvtc"), desc="Launch rxvt-unicode"),
    Key("A-w", lazy.spawn("/usr/local/src/waterfox/waterfox-bin"), desc="Launch waterfox"),
    Key("M-w", lazy.spawn("librewolf"), desc="launch my Browser"),
    Key("A-C-s", lazy.spawn("/usr/local/src/sublime_text/sublime_text"), desc="Launch sublime_text"),
]

groups = [
    Group("1", layout="monadtall"),
    Group("2", layout="monadtall"),
    Group("3", layout="monadtall"),
    Group("4", layout="monadtall"),
    Group("5", layout="max"),
    Group("6", layout="ratiotile"),
]

for k, group in zip(["1", "2", "3", "4", "5", "6"], groups):
    keys.append(Key("M-"+(k), lazy.group[group.name].toscreen()))
    keys.append(Key("M-S-"+(k), lazy.window.togroup(group.name)))

def init_layout_theme():
    return {
            "margin": 10,
            "border_width": 4,
            "border_focus": '#5e81ac',
            "border_normal": '#4c566a'
            }

layout_theme = init_layout_theme()

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, **layout_theme),
    layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Tile(**layout_theme),
    #layout.TreeTab(
    #    sections=['FIRST', 'SECOND'],
    #    bg_color='#3b4252',
    #    active_bg='#bf616a',
    #    inactive_bg='#a3be8c',
    #    padding_y=5,
    #    section_top=10,
    #    panel_width=280
    #),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#Colors for the bar
def init_colors():
    return [["#2e3440", "#2e3440"], # color 0  dark grayish blue
            ["#2e3440", "#2e3440"], # color 1  dark grayish blue
            ["#3b4252", "#3b4252"], # color 2  very dark grayish blue
            ["#434c5e", "#434c5e"], # color 3  very dark grayish blue
            ["#4c566a", "#4c566a"], # color 4  very dark grayish blue
            ["#d8dee9", "#d8dee9"], # color 5  grayish blue
            ["#e5e9f0", "#e5e9f0"], # color 6  light grayish blue
            ["#eceff4", "#eceff4"], # color 7  light grayish blue
            ["#8fbcbb", "#8fbcbb"], # color 8  grayish cyan
            ["#88c0d0", "#88c0d0"], # color 9  desaturated cyan
            ["#81a1c1", "#81a1c1"], # color 10 desaturated blue
            ["#5e81ac", "#5e81ac"], # color 11 dark moderate blue
            ["#bf616a", "#bf616a"], # color 12 slightly desaturated red
            ["#d08770", "#d08770"], # color 13 desaturated red
            ["#ebcb8b", "#ebcb8b"], # color 14 soft orange
            ["#a3be8c", "#a3be8c"], # color 15 desaturated green
            ["#b48ead", "#b48ead"]] # color 16 grayish magenta

colors = init_colors()

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font='Ubuntu Nerd Font',
    fontsize=12,
    padding=8,
    background=colors[0],
    foreground=colors[5]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    background=colors[1], #2e3440
                    foreground=colors[5], #d8dee9
                    linewidth=1,
                    padding=10
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/qtilelogo.png",
                    iconsize=8,
                    background=colors[1],
                    mouse_callbacks={'Button1': lambda : qtile.cmd_spawn('rofi -show run')}
                ),
                widget.Sep(
                    background=colors[1],
                    foreground=colors[5],
                    linewidth=1,
                    padding=10
                ),
                widget.GroupBox(
                    active=colors[16], #b48ead
                    borderwidth=2,
                    disable_drag=True,
                    font='Ubuntu Nerd Font',
                    fontsize=14,
                    hide_unused=False,
                    highlight_method='line',
                    inactive=colors[6], #e5e9f0
                    margin_x=0,
                    margin_y=3,
                    padding_x=5,
                    padding_y=8,
                    rounded=False,
                    this_current_screen_border=colors[14], #ebcb8b
                    urgent_alert_method='line'
                ),
                widget.Sep(
                    background=colors[1],
                    foreground=colors[5],
                    linewidth=1,
                    padding=10
                ),
                widget.CurrentLayoutIcon(
                    background=colors[1],
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[6], #e5e9f0
                    padding=0,
                    scale=0.65
                ),
                widget.Sep(
                    background=colors[1],
                    foreground=colors[5],
                    linewidth=1,
                    padding=10
                ),
                widget.CurrentLayout(
                    background=colors[1],
                    font='Ubuntu Bold',
                    foreground=colors[6]
                ),
                widget.Prompt(
                    background=colors[1],
                    font='Ubuntu',
                    fontsize=12,
                    foreground=colors[6]
                ),
                widget.Spacer(),
                widget.ThermalSensor(
                    foreground=colors[14],
                    update_interval=2,
                    format = ' {temp:.1f}{unit}',
                    fmt = '{}',
                    decorations=[
                        BorderDecoration(
                            colour = colors[14],
                            border_width = [0, 0, 2, 0],
                    )
                ],
                ),
                widget.Spacer(length = 8),
                widget.CPU(
                     format = '   Cpu: {load_percent}%',
                     foreground = colors[8],
                     decorations=[
                        BorderDecoration(
                          colour = colors[8],
                          border_width = [0, 0, 2, 0],
                      )
                  ],
                  ),

                widget.Spacer(length = 8),
                widget.Memory(
                    background=colors[1],
                    font='Ubuntu Nerd Font',
                    fontsize=12,
                    foreground=colors[12],
                    format="  Mem:  {MemUsed: .0f}{mm}",
                    update_interval=1.0,
                    decorations=[
                        BorderDecoration(
                            colour = colors[12],
                            border_width = [0, 0, 2, 0],
                        )
                  ],
                  ),

                widget.Spacer(length = 8),
                widget.DF(
                 update_interval = 60,
                 foreground = colors[14],
                 partition = '/',
                 #format = '[{p}] {uf}{m} ({r:.0f}%)',
                 format = '{uf}{m} free',
                 fmt = '  Disk: {}',
                 visible_on_warn = False,
                 decorations=[
                    BorderDecoration(
                        colour = colors[14],
                        border_width = [0, 0, 2, 0],
                    )
                 ],
                 ),
                widget.Spacer(length = 8),
                widget.Volume(
                    foreground=colors[8],
                    background=colors[1],
                    font='Ubuntu Nerd Font',
                    padding=5,
                    fmt=' Vol: {}',
                    decorations=[
                        BorderDecoration(
                            colour = colors[8],
                            border_width = [0, 0, 2, 0],
                    )
                ],
                ),
                widget.Spacer(length = 8),
                widget.Battery(
                    font="Ubuntu Nerd Font",
                    foreground=colors[12],
                    background=colors[1],
                    padding=0,
                    fmt='   {}',
                    format='{char} {percent:2.0%} {hour:d}:{min:02d}',
                    decorations=[
                        BorderDecoration(
                            colour =colors[12],
                            border_width = [0, 0, 2, 0],
                    )
                ],
                ),
                widget.Spacer(length = 8),
                widget.Clock(
                    background=colors[1],
                    font='Ubuntu',
                    fontsize=12,
                    foreground=colors[14],
                    fmt='  {}',
                    format='%d/%m/%y %H:%M',
                    decorations=[
                        BorderDecoration(
                            colour=colors[14],
                            border_width=[0, 0, 2, 0],
                    )
                ],
                ),
                widget.Spacer(length = 8),
                widget.Systray(
                    background=colors[1],
                    foreground=colors[8],
                    icon_size=20,
                    padding=4
                    ),
            ],
            22,
            opacity=1.0
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag("M-1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front())
]

main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    ],
    border_focus=colors[12] [0]
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

@hook.subscribe.restart
def cleanup():
    shutil.rmtree(os.path.expanduser('~/.config/qtile/__pycache__'))

@hook.subscribe.shutdown
def killall():
    shutil.rmtree(os.path.expanduser('~/.config/qtile/__pycache__'))
    subprocess.Popen(['killall', 'urxvtd', 'lxpolkit', 'nitrogen', 'picom'])

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"




