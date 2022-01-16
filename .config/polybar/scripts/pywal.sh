#!/usr/bin/env bash

# Color files
PFILE="$HOME/.config/polybar/cuts/colors.ini"
RFILE="$HOME/.config/polybar/cuts/scripts/rofi/colors.rasi"
LFILE="$HOME/.config/polybar/cuts/scripts/powermenu.sh"

# Get colors
pywal_get() {
	wal -i "$1" -q -t
}

# Change colors
change_color() {
	# polybar
	sed -i -e "s/background = #.*/background = #${BG}/g" $PFILE
	# sed -i -e "s/background-alt = #.*/background-alt = #8C${BG}/g" $PFILE
	sed -i -e "s/foreground = #.*/foreground = #${FG}/g" $PFILE
	sed -i -e "s/foreground-alt = #.*/foreground-alt = #33${FG}/g" $PFILE
	sed -i -e "s/primary = #.*/primary = $AC/g" $PFILE
	sed -i -e "s/red = #.*/red = $AD/g" $PFILE
	sed -i -e "s/green = #.*/green = $AE/g" $PFILE
	sed -i -e "s/yellow = #.*/yellow = $AF/g" $PFILE
	# sed -i -e "s/i3lock -i .*/i3lock -i $1/g" $LFILE
	
	# rofi
	cat > $RFILE <<- EOF
	/* colors */

	* {
	  al:   #00000000;
	  bg:   #${BG}BF;
	  bga:  #${BG}FF;
	  fg:   #${FG}FF;
	  ac:   ${AC}FF;
	  se:   ${AC}1A;
	}
	EOF
	
	polybar-msg cmd restart
}

# Main
if [[ -f "/usr/bin/wal" ]]; then
	if [[ "$1" ]]; then
		pywal_get "$1"

		# Source the pywal color file
		. "$HOME/.cache/wal/colors.sh"

		BGC=`printf "%s\n" "$background"`
		BG=${BGC:1}
		FGC=`printf "%s\n" "$foreground"`
		FG=${FGC:1}
		AC=`printf "%s\n" "$color1"`
		AD=`printf "%s\n" "$color5"`
		AE=`printf "%s\n" "$color7"`
		AF=`printf "%s\n" "$color6"`

    # Set the border colors.
    bspc config normal_border_color "$color1"
    bspc config active_border_color "$color2"
    bspc config focused_border_color "$color15"
    bspc config presel_feedback_color "$color1"

		change_color
    # wpg -a "$1"
		betterlockscreen -u "$1" -q
		# i3lock -i "$1"
	else
		echo -e "[!] Please enter the path to wallpaper. \n"
		echo "Usage : ./pywal.sh path/to/image"
	fi
else
	echo "[!] 'pywal' is not installed."
fi
