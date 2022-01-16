# start 
if test -n "$DESKTOP_SESSION"
    set -x (gnome-keyring-daemon --start | string split "=")
end

set fish_greeting ""
set -gx TERM xterm-256color
if status is-interactive
    # Commands to run in interactive sessions can go here
end
starship init fish | source

# Aliases
alias ll "exa -abgl --icons"
alias l "exa --icons"
alias lt "exa --tree --icons"
alias gn "goneovim --nvim=/home/mrmango/.local/bin/lvim"
alias nv "lvim"
alias zz "z -c" # restric matches to subdirs of $PWD
alias zi "z -i" # cd with interactive selection
alias zf "z -l" # use fzf to select in multiple matches
alias zb "z -b" # quickly cd to the parent directory
alias py "python"
alias wall "~/.config/polybar/cuts/scripts/pywal.sh"

# Export
set -gx EDITOR ~/.local/bin/lvim
set -gx PATH ~/.local/bin $PATH
set -gx PATH ~/.cargo/bin $PATH
set -gx RANGER_ZLUA ~/z.lua/z.lua
set -gx npm_config_prefix ~/.local
set -gx PF_ASCII "macos"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
# eval /opt/miniconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

# Colors
#if test -e ~/.cache/wal/colors.fish
#    source ~/.cache/wal/colors.fish
#end
