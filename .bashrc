# ____ _______   ______  __  __    _    _   _ ____  
#/ ___|_   _\ \ / /  _ \|  \/  |  / \  | \ | / ___| 
#\___ \ | |  \ V /| |_) | |\/| | / _ \ |  \| \___ \ 
# ___) || |   | | |  _ <| |  | |/ ___ \| |\  |___) |
#|____/ |_|   |_| |_| \_\_|  |_/_/   \_\_| \_|____/ 
#                                                   
# ____    _    ____  _   _ ____   ____ 
#| __ )  / \  / ___|| | | |  _ \ / ___|
#|  _ \ / _ \ \___ \| |_| | |_) | |    
#| |_) / ___ \ ___) |  _  |  _ <| |___ 
#|____/_/   \_\____/|_| |_|_| \_\\____|
#
# My bash config. Use it how you want.
# https://github.com/styrman-g

### EXPORT
export EDITOR=vim
export TERM="xterm-256color"                      # getting proper colors
export GREP_OPTIONS='--color=auto' GREP_COLOR='1;32'
export CLICOLOR=1
export LSCOLORS=ExFxCxDxBxegedabagacad
export PATH="$HOME/.config/emacs/bin:$PATH"

# I also use:
export GREP_OPTIONS='--color=auto' GREP_COLOR='1;32'
export CLICOLOR=1
export LSCOLORS=ExFxCxDxBxegedabagacad

# And if you like colorizing your prompt, defined color vars can be useful:
export COLOR_NC='\e[0m' # No Color
export COLOR_BLACK='\e[0;30m'
export COLOR_GRAY='\e[1;30m'
export COLOR_RED='\e[0;31m'
export COLOR_LIGHT_RED='\e[1;31m'
export COLOR_GREEN='\e[0;32m'
export COLOR_LIGHT_GREEN='\e[1;32m'
export COLOR_BROWN='\e[0;33m'
export COLOR_YELLOW='\e[1;33m'
export COLOR_BLUE='\e[0;34m'
export COLOR_LIGHT_BLUE='\e[1;34m'
export COLOR_PURPLE='\e[0;35m'
export COLOR_LIGHT_PURPLE='\e[1;35m'
export COLOR_CYAN='\e[0;36m'
export COLOR_LIGHT_CYAN='\e[1;36m'
export COLOR_LIGHT_GRAY='\e[0;37m'
export COLOR_WHITE='\e[1;37m'

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# Allows you to cd into directory by typing the directory name.
shopt -s autocd 

# Setting my Bash promt.
#export PS1="\[$(tput bold)\]\[\033[38;5;1m\][\[$(tput sgr0)\]\[\033[38;5;11m\]\u\[$(tput sgr0)\]\[\033[38;5;3m\]@\[$(tput sgr0)\]\[\033[38;5;14m\]\H\[$(tput sgr0)\]\[\033[38;5;1m\]]\[$(tput sgr0)\]\\$\[$(tput sgr0)\] "

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Some aliases
# pacman package manager
alias update='sudo pacman -Syu'
alias install='sudo pacman -S'

# Adding color
alias ls='ls -hN --color=always --group-directories-first'
alias grep="grep --color=auto"

# Internet
# Download video
alias yt="youtube-dl --add-metadata -ic"
# Download only audio
alias yta="youtube-dl --add-metadata -xic"

# Starchip-A cross-shell prompt
eval "$(starship init bash)"

#nerdfetch
fastfetch -c neofetch.jsonc
#neofetch
