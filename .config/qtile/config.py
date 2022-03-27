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
myTerm = 'kitty'

theme = "rosePine"  # only if available in ~/.config/qtile/themes
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


def pavucontrol():
    qtile.cmd_spawn('pavucontrol')


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

groups = [Group(i) for i in ["五", "六", "七", "八", "九"]]

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
#  COLORS #
###########

# Left widgets configure

# Left widget background color
leftBackground = colors['bg1']
# Left widget foreground color
leftForeground = colors['fg']

# Rigth widgets background colors
rightBackground = colors['inactive']
# Rigth widgets font colors
rightForeground = colors['fg']

# Fonts
fontWidget = 'SFMono Bold'
fontIcons = 'Arimo Nerd Font'

###########
# LAYOUTS #
###########

layout_conf = {
    'border_focus': colors['color5'][0],
    'border_width': 2,
    'border_normal': colors['bg'][0],
    'margin': 13
}

layouts = [
    layout.Max(max_rules=[Match(wm_class='peek')]),
    layout.MonadTall(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    layout.Bsp(**layout_conf),
    layout.Stack(
        **layout_conf,
        num_stacks=2,
        fair=True),
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


def base(fg='base', bg='bg'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator(pd=7):
    return {
        'linewidth': 0,
        'padding': pd
    }


group_box = {
    'foreground': leftBackground,
    'background': leftBackground,
    'active': leftForeground,
    'inactive': rightBackground,
    'this_current_screen_border': leftForeground,
    'this_screen_border': colors['color2'],
    "highlight_color": rightBackground,
    "block_highlight_text_color": leftBackground,
    "other_current_screen_border": colors['color2'],
    "other_screen_border": colors['color2'],
    "urgent_border": colors['color4'],
    'fontsize': 15,
    'padding': 0,
    'borderwidth': 3,
    'disable_drag': True,
    'rounded': True,
    'highlight_method': 'block',
    'font': 'Mochiy Pop One',
}

window_name = {
    **base(fg='fg'),
    'font': fontWidget,
    'fontsize': 11,
    'padding': 2
}

systray = {
    'background': leftBackground,
    'padding': 7,
    'icon_size': 15,
}

text_box = {
    'font': fontWidget,
    'fontsize': 13,
    'padding': 3
}

current_layout_icon = {
    'scale': 0.53,
    'background': colors['color4'],
    'padding': -3,
}

current_layout = {
    'padding': 3,
    'font': fontWidget,
    'fontsize': 11,
}

clock = {
    'padding': 0,
    'font': fontWidget,
    'fontsize': 11,
    'format': '%d - %I:%M '
    #  'format': '%b %d - %I:%M '
}

volume_icon = {
    'emoji': True,
    'font': fontIcons,
    'fontsize': 15,
    'padding': 2
}
pomodoro = {
    'background': colors['fg1'],
    'color_active': colors['bg'],
    'color_inactive': colors['bg'],
    'color_break': colors['bg'],
    'padding': 5,
    'fontsize': 13,
    'font': fontWidget,
    'prefix_inactive': 'Work',
    'length_pomodori': 60,
    'length_short_break': 10,
    'length_long_break': 30,
}


def workspaces():
    return [
        widget.Image(
            filename=img['basei']
        ),
        widget.GroupBox(**group_box,),
        widget.Sep(**separator(),
                   **base(bg='bg1')
                   ),
        widget.Image(
            filename=img['basefi']
        ),
        widget.Memory(
            font=fontWidget,
            format='{MemUsed: .0f}M/{MemTotal: .0f}M',
            update_interval=1,
            fontsize=12,
            measure_mem='M',
            foreground=leftBackground,
            background=colors['color5'],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
        ),
        widget.Sep(**separator(),
                   **base(bg='color5')
                   ),
        widget.Image(
            filename=img['color5fi']
        ),
        widget.Sep(**separator(),
                   **base(bg='color3')
                   ),
        widget.CPU(
            font=fontWidget,
            format='CPU {load_percent}%',
            update_interval=1,
            fontsize=12,
            foreground=leftBackground,
            background=colors['color3'],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
        ),
        widget.Image(
            filename=img['color3fi']
        ),
        widget.Sep(**separator(),
                   **base(bg='color4')
                   ),
        widget.CurrentLayoutIcon(
            **current_layout_icon,
            custom_icon_paths=[path.join(qtile_path, "icons")],
        ),
        widget.Sep(**separator(pd=5),
                   **base(bg='color4')
                   ),
        widget.CurrentLayout(
            **base(bg='color4', fg='bg1'),
            **current_layout
        ),
        widget.Image(
            filename=img['color2i']
        ),
        widget.Spacer(),
        widget.Image(
            filename=img['basei']
        ),
        widget.Sep(**separator(pd=4),
                   **base(bg='bg1')
                   ),
        widget.WindowName(
            background=leftBackground,
            fontsize=12,
            font=fontWidget,
            foreground=leftForeground,
            width=bar.CALCULATED,
            empty_group_string=theme,
            max_chars=19,
            format='{class}'
            #  mouse_callbacks={"Button2": kill_window},
        ),
        widget.Sep(**separator(pd=4),
                   **base(bg='bg1')
                   ),
        widget.WindowCount(
            background=leftBackground,
            font=fontWidget,
            foreground=leftForeground,
            fontsize=12,
        ),
        widget.Image(
            filename=img['basef']
        ),
        widget.Spacer(),
    ]


def powerline_base():
    return [
        widget.Image(
            filename=img['color4i']
        ),
        widget.TextBox(
            **base(bg='color4'),
            font=fontIcons,
            fontsize=12,
            padding=4,
            text='',
            mouse_callbacks={"Button1": pavucontrol},
        ),
        widget.Sep(**separator(pd=2),
                   **base(bg='color4')
                   ),
        widget.Sep(**separator(pd=5),
                   **base(bg='inactive')
                   ),
        widget.Volume(
            background=rightBackground,
            foreground=rightForeground,
            padding=3,
            font=fontWidget,
            fontsize=11,
        ),
        widget.Image(
            filename=img['base1f']
        ),
        widget.Sep(**separator(pd=4),
                   background="#00000000",
                   ),
        widget.Image(
            filename=img['color3i']
        ),
        widget.TextBox(
            **base(bg='color3'),
            fontsize=12,
            font=fontIcons,
            padding=2,
            text=''
        ),
        widget.Sep(**separator(pd=4),
                   **base(bg='color3')
                   ),
        widget.Sep(**separator(pd=5),
                   **base(bg='inactive')
                   ),
        widget.Net(
            font=fontWidget,
            fontsize=12,
            # Here enter your network name
            interface=["wlp0s26u1u4"],
            format='{down}↓',
            foreground=rightForeground,
            background=rightBackground,
            padding=0,
        ),
        # widget.Wlan(
        #     interface="wlp0s26u1u4",
        #     format='{quality}%',
        #     max_chars=5,
        #     foreground=rwfc,
        #     font='SFMono Bold',
        #     background=rwbc,
        #     padding=5,
        #     #  mouse_callbacks={"Button1": open_connman},
        # ),
        widget.Image(
            filename=img['base1f']
        ),
        widget.Sep(**separator(pd=4),
                   background="#00000000",
                   ),
        widget.Image(
            filename=img['color5i']
        ),
        widget.TextBox(
            **base(bg='color5'),
            fontsize=11,
            font=fontIcons,
            padding=2,
            text='',
        ),
        widget.Sep(**separator(pd=5),
                   **base(bg='color5')
                   ),
        widget.Sep(**separator(pd=9),
                   background=rightBackground,
                   ),
        widget.Clock(
            **clock,
            background=rightBackground,
            foreground=rightForeground,
        ),
        widget.Image(
            filename=img['base1f']
        ),
        widget.Sep(**separator(pd=4),
                   background="#00000000",
                   ),
        widget.Systray(
            **systray
        ),
        widget.Sep(**separator(pd=9),
                   background="#00000000",
                   ),
        widget.TextBox(
            text="⏻",
            font=fontIcons,
            background=leftBackground,
            foreground=colors['color4'],
            fontsize=14,
            padding=0,
            mouse_callbacks={"Button1": power_menu},
        ),
        widget.Sep(**separator(pd=3),
                   **base(bg='bg1')
                   ),
        widget.Image(
            filename=img['basef']
        ),
    ]


triangle_widgets = [
    *workspaces(),
    *powerline_base(),
]

square_widgets = [
    *workspaces(),
    *powerline_base()
]

widget_defaults = {
    'font': fontWidget,
    'fontsize': 13,
    'padding': 2
}
extension_defaults = widget_defaults.copy()

# SCREENS
# Bar on top-botton of the screen
screens = [
    Screen(top=bar.Bar(
        triangle_widgets,
        21,
        opacity=1,
        background="#00000000",
        margin=[3, 4, 5, 4]
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
        Screen(top=bar.Bar(triangle_widgets, 24, opacity=0.95))
    )

# OTHER STUFF

dgroups_key_binder = None
dgroups_app_rules = []  # type List
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
        Match(wm_class='pavucontrol'),  # pavucontrol
    ],
    border_focus=colors["fg1"][0],
    border_width=0
)
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
