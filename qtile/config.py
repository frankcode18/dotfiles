from typing import List 
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from random import shuffle 

import os
#Tecla principal usada para los comandos(mod1=Alt-izq, mod4=Super-izq)
mod = "mod1"

keys = [
    #Hotkey de la app Dmenu
    Key([mod], "q", lazy.spawn("rofi -show drun")),

    # Cambio del foco entre ventanas
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Teclas personalizadas.
    Key([mod], "c", lazy.spawn("google-chrome-stable")),
    Key([mod], "s", lazy.spawn("subl")),
    Key([mod], "d", lazy.spawn("texmaker")),
    Key([mod], "a", lazy.spawn("android-studio")),
    Key([mod], "v", lazy.spawn("vscodium")),
    Key([mod], "o", lazy.spawn("ms-office-online")),
    Key([mod], "g", lazy.spawn("gimp")),
    Key([mod], "t", lazy.spawn("teams")),
    
    # Mover las ventanas de posicion.
    # Mover fuera del layout de las columnas creara una nueva columna
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Agrandar las ventanas desde el borde a cualquier direccion
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "i", lazy.spawn("kitty"), desc="Launch terminal"),

    # Cambia entre los layouts habilitados 
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    # Screenshot
    # Guardar screenshot al clipboard
    Key([], "Print", lazy.spawn("escrotum -C")),
    # Guardar screenshots a la carpeta
    Key([mod], "Print", lazy.spawn("escrotum ~/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png")),
	# Capturar una region de la pantalla al clipboard
    Key([mod, "shift"], "s", lazy.spawn("escrotum -Cs ")),
]
# Espacios de trabajo 
#groups = [Group(i) for i in ""]
__groups = {
    # Los matches sirven para agregar reglas a los espacios de trabajo.
    1:Group("", matches=[Match(wm_class=["google-chrome"])]),
    2:Group("",matches=[Match(wm_class=["tilix"])]),
    3:Group("",matches=[Match(wm_class=["sublime_text"])]),
    4:Group("",matches=[Match(wm_class=["vscodium","microsoft teams - preview"])]),
    5:Group("",matches=[Match(wm_class=["sun-awt-X11-XWindowPeer","sun-awt-X11-XFramePeer"])]),
    6:Group("",matches=[Match(wm_class=["ms-office-online"])]),
}
# Bucle donde se habilita los espacios de trabajo.
groups = [__groups[i] for i in __groups]

def get_group_key(name):
    # Se agrega un contador para poder usarlas en las hotkeys y poder usar los numeros al cambiar
    # entre espacios de trabajo
    return [k for k, g in __groups.items() if g.name ==name][0]
for i in groups:
    keys.extend([
        # mod = tecla definida anteriormente mas el numero cambiar el espacio de trabajo
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod + shift + el numero del espacio de trabajo cambia la ventana donde se esta trabando a la elejida
        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Si prefieres mover la ventana donde no se esta trabajando a otro espacio de trabajo active lo siguiente
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
# Son formas en las que se organizan las ventanas estan predefinidas pero se pueden editar
layouts = [
    #layout.Columns(),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(
        num_stacks=2,
        fair = True, 
        border_width=2,
        border_focus='#d65d0e',
        margin=6,
        ),
    layout.Bsp(border_width=2,
        border_focus='#d65d0e',
        fair=False,
        grow_amount=3,
        lower_right=True,
        margin=6,
        ),
    #layout.Matrix(),
    layout.MonadTall(
        border_width=2,
        border_focus='#d65d0e',
        single_border_width=2,
        margin=6,
        change_size=20,
        max_ratio=0.75,
        min_ratio=0.40,
        ratio=0.65),
    #layout.MonadWide(
        #border_focus='#85DEC0',
        #single_border_width=3,
        #margin=3,
        #name= ' 鱗',
        #change_size=20,
        #max_ratio=0.75,
        #min_ratio=0.40,
        #ratio=0.6),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(font='Gohufont Nerd Font Bold',
    #    panel_width=90, sections=["臭"]),
    #layout.VerticalTile(),
    #layout.Zoomy(name="Z",
    #    ),

]
#Lista de frases motivadoras:
motiv = ["Da siempre lo mejor de ti, lo que plantes ahora lo cosecharas mas tarde.", 
        "Celebra tus propias Victorias porque nadie mas entiende, lo que te costo alcanzarlas.", 
        "El exito no se mide por lo que logras, sino por los obstaculos que superas.", 
        "Un sueño no se hace realidad por arte de magia, necesita sudor, determinación y trabajo duro - Colin Powell",
        "No busques los errores, busca un remedio - Henry Ford",
        "Si te caíste ayer, levántate hoy - H. G. Wells",
        "Siempre parece imposible... hasta que se hace - Nelson Mandela",
        "No cuentes los días, haz que los días cuenten - Muhammad Ali",
        "Los obstáculos son esas cosas atemorizantes que ves cuando apartas los ojos de tu meta - Henry Ford"]

shuffle(motiv)
frases = motiv[0]

#Colores Gruvbox
colors = [["#282828", "#282828"], # negro-background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#000000", "#000000"], # fg 
          ["#ea6962", "#ea6962"], # rojo 
          ["#a9b665", "#a9b665"], # verde 
          ["#e78a4e", "#e78a4e"], # amarillo 
          ["#7daea3", "#7daea3"], # azul
          ["#d3869b", "#d3869b"]] # morado 
widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=13,
    padding=2,
)
extension_defaults = widget_defaults.copy()
# La barra inferior, se puede agregar a otra pantalla creando otra barra
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    block_highlight_text_color = colors[3] ,
                    borderwidth = 0,
                    disable_drag = True,
                    active = colors[4],
                    fontsize = 22,
                    margin = 4.5,
                    ),
                widget.WindowName(
                     foreground = colors[5] ,
                     fontsize=13.5,
                     empty_group_string=frases,
                     format = '{empty}'),
                     #para saber el wm_class
                #     #format = '{class}'),
                widget.Systray(),
                widget.TextBox(
                       text = '',
                       foreground = "#cc241d",
                       padding = 0,
                       margin = 0,
                       fontsize = 37
                       ),
                widget.Spacer(length=2,width=None,foreground = colors[2],background = "#cc241d"),
                widget.CurrentLayout(
                    foreground = colors[2],
                    background = "#cc241d",
                    padding= 5,
                    font="FantasqueSansMono Nerd Font Mono Regular",
                    fontsize=14.5,),
                widget.Wallpaper(directory = '~/Pictures/Wallpapers', label='',
                    fontsize = 22,foreground = colors[2],background = "#cc241d"),
                widget.TextBox(
                       text = '',
                       background = "#cc241d",
                       foreground = "#98971a",
                       padding = 0,
                       margin = 0,
                       fontsize = 37
                       ),
                widget.Memory(
                       foreground = colors[2],
                       background = "#98971a",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(tilix + ' -e htop')},
                       padding = 5,
                       fontsize = 13,
                       font="FantasqueSansMono Nerd Font Mono Regular",
                       ),
                widget.TextBox(
                       text = '',
                       background = "#98971a",
                       foreground = "#d79921",
                       padding = 0,
                       margin = 0,
                       fontsize = 37
                       ),
                widget.Clock(
                    format='%Y-%m-%d'' - ''%I:%M %p',
                    font="FantasqueSansMono Nerd Font Mono Regular",
                    fontsize=13.5,
                    foreground = colors[2],
                    background = "#d79921",
                    margin = 1
                    ),
                widget.TextBox(
                    text = '',
                    background = "#d79921",
                    foreground = "#458588",
                    padding = 0,
                    margin = 0,
                    fontsize = 37
                    ),
                widget.Volume(emoji=True, foreground = colors[2], fontsize=14,background = "#458588"),
                widget.Volume(              
                    foreground = colors[2],  
                    background = "#458588",  
                    padding = 1,
                    fontsize = 14,
                    font="FantasqueSansMono Nerd Font Mono Regular",
                    ),  
                #widget.QuickExit(foreground="#CC00FF", default_text="   ", fontsize = 23),
                widget.Spacer(length=10,width=None,foreground = colors[2],background = "#458588")
            ],
            20,
            #opacity = 9
        ),
    ),
]

# Mover las ventanas y hacerlas flotantes.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
   
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_focus='#85DEC0',border_width=2,
        float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

#Mantener el nombre del windows manager en LG3D para evitar problemas con algunas
#apps que se ejecutan con java.

wmname = "LG3D"

# Por si desactivo el widget de los wallpapers > feh --bg-fill Pictures/Wallpapers/wal3.png
#inicio = [
#        "picom --experimental-backends & ",
#]
#for x in inicio:
#    os.system(x)
#for handling android studio hiding itself
#hook.subscribe.client_name_updated
def fixAndroidStudio(w):
    if wm_class == 'sun-awt-X11-XWindowPeer' or 'sun-awt-X11-XFramePeer':
        for i in range(5):
            time.sleep(5)
            w.unhide()
