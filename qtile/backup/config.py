from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, qtile
from os import listdir
from os import path
import subprocess
import json

qtile_path = path.join(path.expanduser("~"), ".config", "qtile")

#########
# THEME #
#########

theme = "rosePineDawn"  # only if available in ~/.config/qtile/themes
theme_path = path.join(qtile_path, "themes", theme)

# COLOR SCHEME - map color name to hex values
with open(path.join(theme_path, "colors.json")) as f:
    colors = json.load(f)
img = {}

# IMAGE-THEME - map image name to its path
img_path = path.join(theme_path, "img")
for i in listdir(img_path):
    img[i.split(".")[0]] = path.join(img_path, i)

#############
# AUTOSTART #
#############


@hook.subscribe.startup_once
def autostart():
    script = path.join(qtile_path, "autostart.sh")
    subprocess.call([script])


def open_launcher():
    qtile.cmd_spawn('./.config/rofi/scripts/apps.sh')
def power_menu():
    qtile.cmd_spawn('./.config/rofi/applets/applets/powermenu.sh')

#  @hook.subscribe.client_new
#  def floating_size_hints(window):
#      hints = window.window.get_wm_normal_hints()
#      if hints and 0 < hints['max_width'] < 1000:
#          window.floating = True

########
# KEYS #
########

#  mod1 = Alt key, mod4 = Super key


mod = "mod1"

#          Special  KeyCap  Actions
keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Screenshots
    ([], "Print", lazy.spawn("escrotum -C")),
    ([mod], "Print", lazy.spawn("escrotum ~/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png")),
    ([mod, "shift"], "s", lazy.spawn("escrotum -s ")),

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod], "n", lazy.layout.normalize()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod], "space", lazy.layout.next()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),

    # Qtile
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "0", lazy.spawn("./.config/rofi/applets/applets/powermenu.sh")),


    # Swap panes of split stack
    ([mod, "shift"], "space", lazy.layout.rotate()),
    ([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # ------------ Apps Configs ------------

    ([mod], "w", lazy.window.kill()),
    #  ([mod], "q", lazy.spawn("rofi -show run")),
    ([mod], "q", lazy.spawn("./.config/rofi/scripts/apps.sh")),
    ([mod], "o", lazy.spawn("ms-office-online")),
    ([mod], "t", lazy.spawn("teams")),
    ([mod], "m", lazy.spawn("theme-changer.sh")),
    ([mod], "i", lazy.spawn("kitty --single-instance")),
    ([mod], "f", lazy.window.toggle_fullscreen()),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

# MOUSE
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

##########
# GROUPS #
##########

groups = [Group(i) for i in [(""), "", "", "", ""]]

for i, group in enumerate(groups):
    # Each workspace is identified by a number starting at 1
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N (actual_key)
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N (actual_key)
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

###########
# LAYOUTS #
###########

layout_conf = {
    'border_focus': colors['blue'][0],
    'border_width': 2,
    'border_normal': colors['bg'][0],
    'margin': 13
}

layouts = [
    layout.Max(max_rules=[Match(wm_class='peek')]),
    layout.MonadTall(**layout_conf),
    #layout.MonadWide(**layout_conf),
    #layout.Matrix(columns=2, **layout_conf),
    layout.Bsp(**layout_conf),
    layout.Stack(
        **layout_conf,
        num_stacks=2,
        fair = True),
    # layout.Columns(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

###########
# WIDGETS #
###########

# Reusable configs for displaying different widgets on different screens


def base(fg='bg0', bg='bg'):
    return{
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator(pd=7):
    return {
        'linewidth': 0,
        'padding': pd
    }


group_box = {
    'foreground': colors['fg'],
    'background': colors['blue'],
    'active': colors['bg0'],
    'inactive': colors['bg3'],
    'this_current_screen_border': colors['bg'],
    'this_screen_border': colors['red'],
    "highlight_color": colors['bg3'],
    "block_highlight_text_color": colors['fg'],
    "other_current_screen_border": colors['yellow'],
    "other_screen_border": colors['yellow'],
    "urgent_border": colors['yellow'],
    'fontsize': 21,
    'padding': 0,
    'borderwidth': 6,
    'disable_drag' : True,
    'rounded': True,
    'highlight_method': 'block',
    'font': 'Font Awesome Bold',
}

window_name = {
    **base(fg='fg'),
    'font': 'Font Awesome',
    'fontsize': 11,
    'padding': 2
}

systray = {
    'background':"#00000000",
    'padding': 5
}

text_box = {
    'font': 'Font Awesome',
    'fontsize': 13,
    'padding': 3
}

current_layout_icon = {
    'scale': 0.50,
    'background': colors['bg1'],
    'padding': -3,
}

current_layout = {
    'padding': 3,
    'font': 'Font Awesome',
}

clock = {
    'padding': 0,
    'font': 'Font Awesome',
    'format': '%d - %I:%M '
    #  'format': '%b %d - %I:%M '
}

volume_icon = {
     'emoji': True,
     'font': 'Font Awesome',
     'fontsize': 11,
     'padding': 2
}
pomodoro = {
    'background': colors['fg3'],
    'color_active': colors['bg'],
    'color_inactive': colors['bg'],
    'color_break': colors['bg'],
    'padding': 5,
    'fontsize': 13,
    'font': 'Font Awesome',
    'prefix_inactive': 'Work',
    'length_pomodori': 60,
    'length_short_break': 10,
    'length_long_break': 30,
}


def workspaces():
    return [
        widget.Image(
            filename=img['blueff']
        ),
        # widget.TextBox(
        #     text="",
        #     foreground=colors['fg'],
        #     background=colors['bg1'],
        #     font="Font Awesome 5 Free Solid",
        #     fontsize=18,
        #     padding=5,
        #     mouse_callbacks={"Button1":open_launcher},
        # ),
        # widget.Sep(**separator(pd=3),
        #     **base(bg='bg1')
        # ),
        #  widget.TextBox(
        #      text="",
        #      foreground=colors['blue'],
        #      background=colors['bg1'],
        #      fontsize=21,
        #      padding=0,
        #  ),
        widget.GroupBox(**group_box,
            #  font="Font Awesome 5 Brands",
        ),
        widget.Image(
            filename=img['bluei']
        ),
        widget.Sep(**separator(),
            **base(bg='bg1')),
        widget.CurrentLayoutIcon(
            **current_layout_icon,
        ),
        widget.Sep(**separator(pd=5),
            **base(bg='bg1')
        ),
        widget.CurrentLayout(
            **base(bg='bg1',fg='fg'),
            **current_layout
        ),
        widget.Image(
            filename=img['darkf']
        ),
        widget.Systray(
            **systray
        ),
        widget.Spacer(),
        widget.Image(
            filename=img['darki']
        ),
        widget.Sep(**separator(pd=4),
            **base(bg='bg1')
        ),
        widget.TextBox(
            text=" ",
            background=colors['bg1'],
            # background="#00000000",
            foreground=colors['fg'],
            fontsize=9,
            font="Font Awesome 5 Free Solid",
        ),
        widget.WindowName(
            background=colors['bg1'],
            fontsize=12,
            foreground=colors['fg'],
            width=bar.CALCULATED,
            empty_group_string="Desktop",
            max_chars=15,
            format='{class}'
            #  mouse_callbacks={"Button2": kill_window},
        ),
        widget.Sep(**separator(pd=4),
            **base(bg='bg1')
        ),
        widget.WindowCount(
            background=colors['bg1'],
            foreground=colors['fg'],
            fontsize=12,
        ),
        widget.Image(
            filename=img['darkf']
        ),
        widget.Spacer(),
    ]

def powerline_base():
    return [
        widget.Image(
            filename=img['redf']
        ),
        widget.TextBox(
            **base(bg='red'),
            fontsize=18,
            padding=4,
            text=''
        ),
        widget.Sep(**separator(pd=2),
            **base(bg='red')
        ),
        widget.Volume(
            **base(bg='red'),
            padding=3,
            font= 'FontAwesome',
        ),
        widget.Image(
            filename=img['redi']
        ),
        widget.Sep(**separator(pd=3),
            background="#00000000",
        ),
        widget.Image(
            filename=img['wbluef']
        ),
        widget.TextBox(
            **base(bg='aqua'),
            fontsize=19,
            padding=5,
            text=''
        ),
        widget.Wlan(
            interface="wlp0s26u1u4",
            format="{essid}",
            max_chars=5,
            foreground=colors['bg0'],
            background=colors['aqua'],
            padding=5,
            #  mouse_callbacks={"Button1": open_connman},
        ),
        widget.Image(
            filename=img['wbluei']
        ),
        widget.Sep(**separator(pd=3),
            background="#00000000",
        ),
        widget.Image(
            filename=img['yellowf']
        ),
        widget.Sep(**separator(pd=3),
            **base(bg='yellow')
        ),
        widget.TextBox(
            **base(bg='yellow'),
            fontsize=15,
            padding=2,
            text='',
        ),
        widget.Sep(**separator(pd=4),
            **base(bg='yellow')),
        widget.Clock(
            **base(bg='yellow'),
            **clock,
        ),
        widget.Sep(**separator(pd=5),
            **base(bg='yellow')
        ),
        widget.Sep(**separator(pd=5),
            **base(bg='bg1')
        ),
        widget.Sep(**separator(pd=3),
            **base(bg='bg1')
        ),
        widget.TextBox(
            text="⏻",
            foreground=colors['fg'],
            background=colors['bg1'],
            font="Font Awesome 5 Free Solid",
            fontsize=14,
            padding=0,
            mouse_callbacks={"Button1": power_menu},
        ),
        widget.Image(
            filename=img['darkf']
        ),
    ]


triangle_widgets = [
    *workspaces(),
    *powerline_base(),
 ]


square_widgets= [
    *workspaces(),
    *powerline_base()
]

widget_defaults = {
    'font': 'FontAwesome',
    'fontsize': 13,
    'padding': 2
}
extension_defaults = widget_defaults.copy()


# SCREENS
# Bar on top-botton of the screen
screens = [
    Screen(top=bar.Bar(
        triangle_widgets,
        20,
        opacity=1,
        background="#00000000",
        margin=[3,4,5,4]
    )),
]
#  if theme=="gruvboxDark":
#      screens = [
#          Screen(top=bar.Bar(triangle_widgets, 22, opacity=1))
#      ]
#  else:
#      screens = [
#          Screen(top=bar.Bar(square_widgets, 22, opacity=1))
#      ]

# check connected monitors
monitors_status = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1]

if monitors_status.count("connected") == 2:
    screens.append(
        Screen(top=bar.Bar(monitor_widgets, 24, opacity=0.95))
    )

# OTHER STUFF

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
        float_rules=[
 # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='confirm'),  # gitk
    Match(wm_class='dialog'),  # gitk
    Match(wm_class='download'),  # gitk
    Match(wm_class='error'),  # ssh-askpass
    Match(title='file_progress'),  # gitk
    Match(title='notification'),  # GPG key password entry
    Match(wm_class='splash'),  # ssh-askpass
    Match(wm_class='toolbar'),  # ssh-askpass
    Match(wm_class='nitrogen'),  # nitrogen
    ],
    border_focus=colors["fg3"][0],
    border_width=0
)
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
