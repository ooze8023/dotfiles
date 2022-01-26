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
import os, subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, EzKey, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer

#from powerline.bindings.qtile.widget import PowerlineText


mod = "mod4"
terminal = guess_terminal()
home = os.path.expanduser('~')

BLACK = "#171717"
RED = "#FF5E5E"
YELLOW = "#F0E68C"
BLUE =   "#50f17a"
MAGENTA = "#E88CFF"
CYAN = "#87CEFA"
WHITE = "#DCDCCC"






keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "space", lazy.layout.next()),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    Key([mod], "n", lazy.layout.normalize()),

    #monad tall
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    #Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    #Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "o", lazy.layout.maximize()),

    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed

    Key([mod, "control"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),

    # Toggle between different layouts as defined below

    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "c", lazy.window.kill()),

    # Comandi generali

    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Rofi
    Key([mod], "f", lazy.spawn("./Fbrofi.sh")),
    Key([mod], "p", lazy.spawn("./Drofi.sh")),
    Key([mod], "w", lazy.spawn("./Wrofi.sh")),

    # capture screen
    Key([mod], "s", lazy.spawn("./shot.sh")),

    # keybord layout
    Key([mod], "t", lazy.widget["keyboardlayout"].next_keyboard()),

    # lanciatori applicazioni
    Key([mod, "control"], "1", lazy.spawn("firefox")),
    Key([mod, "control"], "2", lazy.spawn("./nfm.sh")),
    Key([mod, "control"], "3", lazy.spawn("./vim.sh")),
    Key([mod, "control"], "4", lazy.spawn("pcmanfm")),
    Key([mod, "control"], "5", lazy.spawn("code")),
    Key([mod, "control"], "6", lazy.spawn("gwenview")),
    Key([mod, "control"], "7", lazy.spawn("./htop.sh")),
    Key([mod, "control"], "8", lazy.spawn("./fmui.sh")),
    Key([mod, "control"], "9", lazy.spawn("./mocp.sh")),

    Key([mod, "control"], "0", lazy.spawn("./touchpadt.sh")),

    #wifi
    Key([mod, "control"], "p", lazy.spawn("./wifip.sh")),
    Key([mod, "control"], "t", lazy.spawn("./wifit.sh")),

    #clipmenu
    Key([mod], "a", lazy.spawn('clipmenu  -b  -p "clipboard<" -sb "#AF87FF"')),
    Key([mod], "c", lazy.spawn("./Clip.sh")),

    #toogle top bar
    Key([mod], "b",lazy.hide_show_bar("top"), desc='toggle top bar'),

    #dmenu-aliases
    Key([mod], 'd', lazy.spawn("./dmenu-aliases-zsh.sh")),
    #DropDown term
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('term')),


    EzKey("M-A-w", lazy.run_extension(extension.WindowList(
        item_format="{group}: {window}",
        dmenu_bottom=True,
        foreground="#af87ff",
        selected_background="#af87ff",
        selected_foreground=BLACK,
        font= 'droid sans Mono Bold')),
        desc='window list'),

    EzKey("M-A-c", lazy.run_extension(extension.Dmenu(
        dmenu_command="clipmenu",
        dmenu_bottom=True,
        foreground="#af87ff",
        selected_background="#af87ff",
        selected_foreground=BLACK,
        font= 'droid sans Mono Bold')),
        desc='clipmenu'),

    EzKey("M-A-p", lazy.run_extension(extension.Dmenu(
        dmenu_command="./dmenu-aliases-zsh.sh",
        foreground="#af87ff",
        selected_background="#af87ff",
        selected_foreground=BLACK,
        font= 'droid sans Mono Bold')),
        desc='passmenu'),

    EzKey("M-A-n", lazy.run_extension(extension.Dmenu(
        dmenu_command="networkmanager_dmenu",
        foreground=RED,
        selected_background=RED)),
        desc='dmenu networking'),

    EzKey("M-A-m", lazy.run_extension(extension.CommandSet(
        commands={
            'play/pause': 'mocp -G',
            'next': 'mocp -f',
            'previous': 'mocp -r',
            'quit': 'mocp -x',
            'repeat': 'mocp -t repeat',
            },
        pre_commands=['[ $(mocp -i | wc -l) -lt 1 ] && mocp -S'],
        foreground="#af87ff",
        selected_background="#af87ff",
        selected_foreground=BLACK,
        font= 'droid sans Mono Bold',
        dmenu_bottom=True,)),
        desc='dmenu MOC'),

    EzKey("M-A-q", lazy.run_extension(extension.CommandSet(
        commands={
            'lock': 'slock',
           # 'suspend': 'systemctl suspend && slock',
            'restart': 'reboot',
            'halt': 'systemctl poweroff',
            'logout': 'qtile-cmd -o cmd -f shutdown',
            'reload': 'qtile-cmd -o cmd -f restart',
            },
        foreground="#af87ff",
        selected_background="#af87ff",
        selected_foreground=BLACK,
        font= 'droid sans Mono Bold',
        dmenu_bottom=True,)),
        desc='dmenu session manager'),

    EzKey("M-A-l", lazy.run_extension(extension.CommandSet(
        commands={
            'home ': 'alacritty -e vim &',
            '.config ': 'alacritty -e vim .config &',
            'note': 'alacritty -e vim Note &',
            },
        dmenu_bottom=True,
        foreground="#af87ff",
        selected_background="#af87ff",
        selected_foreground=BLACK,
        font= 'droid sans Mono Bold')),
        desc='dmenu quicklaunch'),


       ]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])
groups.append(
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "/usr/bin/alacritty", opacity=0.8, height=0.76, width=0.66, x=0.17),
    ]), )

#groups.extend([
#        Group('11', spawn='firefox',layout='max', persist=False,
#              matches=[Match(wm_class=['Firefox',])]),
#])
layouts = [

    layout.MonadTall(border_focus='#af87ff', border_color='#000000', borderwidth=2,single_border_width=0, change_ratio=0.1, margin=8, max_ratio=0.8, min_ratio=0.2, ratio=0.5),

    layout.Columns(border_focus_stack=['#56fefe'], border_normal="#000000", border_normal_stack="#000000", border_width=2, border_focus='#af87ff', margin=[8,4,4,8]),

    layout.Max(),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(border_width=1,border_focus='#f3ab61'),
    #layout.Matrix(),
        # layout.RatioTile(),
    #layout.Tile(ratio=0.50, masterWindows=2,border_width=1,border_focus='#AF87FF'),
    layout.TreeTab(section_fg="#AF87FF", active_bg="#AF87FF", active_fg="#f3ab61", fontsize=10),
    # layout.VerticalTile(),
    #layout.Zoomy(),
    layout.Floating(border_focus='#f3ab61', border_normal='#f3ab61'),

]

class ThermalSensor(widget.ThermalSensor):
	def poll(self):
		temp_values = self.get_temp_sensors()
		if temp_values is None:
			return '---'
		no = int(float(temp_values.get(self.tag_sensor, [0])[0]))
		return '{}{}'.format(no, '°')#chr(0x1F321))



widget_defaults = dict(
font='droid sans Mono Bold',
    fontsize= '20',
    padding=0,
)
extension_defaults = widget_defaults.copy()


screens = [


    Screen(

        top =bar.Bar(



            [     widget.TextBox(text="\ue0b0",foreground='#F65E5F', background="#000000",fonts="droid sans mono for powerline",fontsize=20,padding=2),


                   widget.CurrentLayoutIcon(scale=0.65,background="#000000"),

                   widget.TextBox(text="\ue0b0",foreground="#000000", background="#af87ff",fonts="droid sans mono for powerline",fontsize=30),



                widget.TaskList(borderwidth=1 ,border='#000000',background='#af87ff',foreground="#ffffff",highlight_method='block',fontsize=20,max_title_width=160,padding=2),
                widget.TextBox(text="\ue0b0",foreground="#af87ff", background="#000000",fonts="droid sans mono for powerline",fontsize=30),

                widget.TextBox(text="\ue0b0",foreground='#F65E5F', background="#000000",fonts="droid sans mono for powerline",fontsize=10,padding=2),


#                   widget.TextBox(text="\ue0b0",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=15,padding=2),



                widget.GroupBox(active="56fefe" ,borderwidth=1 ,this_current_screen_border="#000000",fontsize=14,this_screen_border="#000000", margin= 4, padding= 4, background= "#000000",highlight_method="line",highlight_color=["000000","#af87ff"],rouded=True),

                #widget.Sep(padding=60,foregroud="#af87ff",backgroud="#000000"),


                #widget.TextBox(text="\ue0b2",foreground="#fe46a5", background="#000000",fonts="droid sans mono for powerline",fontsize=30),

                #widget.Battery(foreground="#000000", background="#fe46a5",format='{char} {percent:2.0%} {hour:d}:{min:02d}',full_char = '=',),

                #widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#fe46a5",fonts="droid sans mono for powerline",fontsize=30),
                #widget.Net(interface='wlp3s0', foreground= "#000000",background="#564acc",),



                   widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#000000",fonts="droid sans mono for powerline",fontsize=10,padding=2),

 #                  widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#000000",fonts="droid sans mono for powerline",fontsize=20,padding=2),



                 widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),

                 widget.Battery(foreground="#000000", background="#af87ff",format='{char} {percent:2.0%} {min:02d}',full_char = '=',padding=8),
           #      widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30,padding=0),

                # widget.TextBox(text="\ue0b0",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=15,padding=2),


#                widget.Wlan(foreground='#af87ff', format= '{quality}/70', disconnected_message='Off',interface='wlp3s0', background='#000000',padding=8),

               # widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30),
               # widget.TextBox(text="\ue0b2",foreground='#fe46a5', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),


            #    widget.TextBox(text="\ue0b2",foreground='#', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),



#                   widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=20,padding=0),


#                widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=20,padding=0),


                 widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30,padding=0),

                   widget.Moc(background="#000000",play_color="#af87ff",noplay_color="#af87ff",padding=8),

                  # widget.TextBox(text="\ue0b0",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),


                widget.TextBox(text="\ue0b2",foreground='#af86ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),

                widget.Volume(update_interval=2, background="#af87ff",foreground="#000000",padding=4),

                widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30,padding=0),


#                widget.TextBox(text="\ue0b0",foreground='#000000', background="#fe46a5",fonts="droid sans mono for powerline",fontsize=20,padding=0),



#                widget.TextBox(text="\ue0b0",foreground='#fe46a5', background="#000000",fonts="droid sans mono for powerline",fontsize=20),

#                widget.TextBox(text="\ue0b0",foreground='#fe46a5', background="#00000000",fonts="droid sans mono for powerline",fontsize=20,padding=2),


                   widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=10,padding=0),

               #ThermalSensor(background="#fe46a5",foreground="#000000",padding=4),


		        widget.CPUGraph(
                    width=30,
                    border_width=1,
                    border_color="#000000",
                    frequency=5,
                    line_width=1,
                    samples=50,
                    graph_color="#F65E5F",
                    fill_color="#F65E5F",
                    type='linefill',
                    sample=100,
                    background="#00000000"
                ),
                widget.MemoryGraph(
                    width=30,
                    border_width=1,
                    border_color="#000000",
                    line_width=1,
                    frequency=5,
                    fill_color="#AF87FF",
                    graph_color="#AF87FF",
                    background="#00000000"

                ),
                widget.NetGraph(
					border_color="#000000",
					line_width=1,
					border_width=1,
					samples=60,
                    graph_color="#56fefe",
                    fill_color="#56fefe",
                    type='linefill',
                    background="#00000000"
				),
                 widget.HDDBusyGraph( width=30,
                    border_width=1,
                    border_color="#000000",
                    line_width=1,
                    frequency=5,
                    fill_color="#fe46a5",
                    graph_color="#fe46a5",
                    background="#00000000"
                ),

                 widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=10,padding=2),


#                 widget.TextBox(text="\ue0b2",foreground='#fe46a5', background="#00000000",fonts="droid sans mono for powerline",fontsize=20,padding=2),



                widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#00000000",fonts="droid sans mono for powerline",fontsize=30),

                ThermalSensor(background="#af87ff",foreground="#000000",padding=4),

                widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30),

				widget.Clock(format='%I:%M %p%a %d-%m-%Y',background="#000000",foreground="#af87ff",padding=8),

                widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30),

				widget.KeyboardLayout(background="#af87ff",foreground="#000000",configured_keyboards=['us','it'],padding=8),

                widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30),

                widget.QuickExit(background="#000000",foreground="#F65E5F",default_text='K',countdown_format='{}',padding=2),

               # widget.TextBox(backgroud="#000000",foregroud="",padding=2),

               widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=15,padding=2),


            ],
            30,

           margin =[6,4,0,4]
        ),
        ),


    Screen(

        top =bar.Bar(



            [     widget.TextBox(text="\ue0b0",foreground='#F65E5F', background="#000000",fonts="droid sans mono for powerline",fontsize=20,padding=2),


                   widget.CurrentLayoutIcon(scale=0.65,background="#000000"),

                   widget.TextBox(text="\ue0b0",foreground="#000000", background="#af87ff",fonts="droid sans mono for powerline",fontsize=30),



                widget.TaskList(borderwidth=1 ,border='#000000',background='#af87ff',foreground="#ffffff",highlight_method='block',fontsize=20,max_title_width=160,padding=2),
                widget.TextBox(text="\ue0b0",foreground="#af87ff", background="#000000",fonts="droid sans mono for powerline",fontsize=30),

                widget.TextBox(text="\ue0b0",foreground='#F65E5F', background="#000000",fonts="droid sans mono for powerline",fontsize=10,padding=2),


#                   widget.TextBox(text="\ue0b0",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=15,padding=2),



                widget.GroupBox(active="56fefe" ,borderwidth=1 ,this_current_screen_border="#000000",fontsize=14,this_screen_border="#000000", margin= 4, padding= 4, background= "#000000",highlight_method="line",highlight_color=["000000","#af87ff"],rouded=True),

                #widget.Sep(padding=60,foregroud="#af87ff",backgroud="#000000"),


                #widget.TextBox(text="\ue0b2",foreground="#fe46a5", background="#000000",fonts="droid sans mono for powerline",fontsize=30),

                #widget.Battery(foreground="#000000", background="#fe46a5",format='{char} {percent:2.0%} {hour:d}:{min:02d}',full_char = '=',),

                #widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#fe46a5",fonts="droid sans mono for powerline",fontsize=30),
                #widget.Net(interface='wlp3s0', foreground= "#000000",background="#564acc",),



                   widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#000000",fonts="droid sans mono for powerline",fontsize=10,padding=2),

 #                  widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#000000",fonts="droid sans mono for powerline",fontsize=20,padding=2),



                 widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),

                 widget.Battery(foreground="#000000", background="#af87ff",format='{char} {percent:2.0%} {min:02d}',full_char = '=',padding=8),
           #      widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30,padding=0),

                # widget.TextBox(text="\ue0b0",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=15,padding=2),


#                widget.Wlan(foreground='#af87ff', format= '{quality}/70', disconnected_message='Off',interface='wlp3s0', background='#000000',padding=8),

               # widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30),
               # widget.TextBox(text="\ue0b2",foreground='#fe46a5', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),


            #    widget.TextBox(text="\ue0b2",foreground='#', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),



#                   widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=20,padding=0),


#                widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=20,padding=0),


                 widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30,padding=0),

                   widget.Moc(background="#000000",play_color="#af87ff",noplay_color="#af87ff",padding=8),

                  # widget.TextBox(text="\ue0b0",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),


                widget.TextBox(text="\ue0b2",foreground='#af86ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30,padding=0),

                widget.Volume(update_interval=2, background="#af87ff",foreground="#000000",padding=4),

                widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30,padding=0),


#                widget.TextBox(text="\ue0b0",foreground='#000000', background="#fe46a5",fonts="droid sans mono for powerline",fontsize=20,padding=0),



#                widget.TextBox(text="\ue0b0",foreground='#fe46a5', background="#000000",fonts="droid sans mono for powerline",fontsize=20),

#                widget.TextBox(text="\ue0b0",foreground='#fe46a5', background="#00000000",fonts="droid sans mono for powerline",fontsize=20,padding=2),


                   widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=10,padding=0),

               #ThermalSensor(background="#fe46a5",foreground="#000000",padding=4),


		        widget.CPUGraph(
                    width=30,
                    border_width=1,
                    border_color="#000000",
                    frequency=5,
                    line_width=1,
                    samples=50,
                    graph_color="#F65E5F",
                    fill_color="#F65E5F",
                    type='linefill',
                    sample=100,
                    background="#00000000"
                ),
                widget.MemoryGraph(
                    width=30,
                    border_width=1,
                    border_color="#000000",
                    line_width=1,
                    frequency=5,
                    fill_color="#AF87FF",
                    graph_color="#AF87FF",
                    background="#00000000"

                ),
                widget.NetGraph(
					border_color="#000000",
					line_width=1,
					border_width=1,
					samples=60,
                    graph_color="#56fefe",
                    fill_color="#56fefe",
                    type='linefill',
                    background="#00000000"
				),
                 widget.HDDBusyGraph( width=30,
                    border_width=1,
                    border_color="#000000",
                    line_width=1,
                    frequency=5,
                    fill_color="#fe46a5",
                    graph_color="#fe46a5",
                    background="#00000000"
                ),

                 widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=10,padding=2),


#                 widget.TextBox(text="\ue0b2",foreground='#fe46a5', background="#00000000",fonts="droid sans mono for powerline",fontsize=20,padding=2),



                widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#00000000",fonts="droid sans mono for powerline",fontsize=30),

                ThermalSensor(background="#af87ff",foreground="#000000",padding=4),

                widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30),

				widget.Clock(format='%I:%M %p%a %d-%m-%Y',background="#000000",foreground="#af87ff",padding=8),

                widget.TextBox(text="\ue0b2",foreground='#af87ff', background="#000000",fonts="droid sans mono for powerline",fontsize=30),

				widget.KeyboardLayout(background="#af87ff",foreground="#000000",configured_keyboards=['us','it'],padding=8),

                widget.TextBox(text="\ue0b2",foreground='#000000', background="#af87ff",fonts="droid sans mono for powerline",fontsize=30),

                widget.QuickExit(background="#000000",foreground="#F65E5F",default_text='K',countdown_format='{}',padding=2),

               # widget.TextBox(backgroud="#000000",foregroud="",padding=2),

               widget.TextBox(text="\ue0b2",foreground='#F65E5F', background="#00000000",fonts="droid sans mono for powerline",fontsize=15,padding=2),


            ],
            25,

           margin = 8,
        ),
        )
    ]




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
    Match(title='pinentry')  # GPG key password
])
floating_layout = layout.Floating(border_width=0)


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

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

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

@hook.subscribe.startup_once
def startup_once():
    commands.reload_screen()


@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    commands.reload_screen()
    qtile.cmd_restart()


