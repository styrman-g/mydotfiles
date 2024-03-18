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
# My bash config. Use it how your want.

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# Allows you to cd into directory by typing the directory name.
shopt -s autocd 

# Setting my Bash promt.
export PS1="\[$(tput bold)\]\[\033[38;5;1m\][\[$(tput sgr0)\]\[\033[38;5;11m\]\u\[$(tput sgr0)\]\[\033[38;5;3m\]@\[$(tput sgr0)\]\[\033[38;5;14m\]\H\[$(tput sgr0)\]\[\033[38;5;1m\]]\[$(tput sgr0)\]\\$\[$(tput sgr0)\] "

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000


# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize


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
alias ls='ls -hN --color=auto --group-directories-first'
alias grep="grep --color=auto"

# Internet
# Download video
alias yt="youtube-dl --add-metadata -ic"
# Download only audio
alias yta="youtube-dl --add-metadata -xic"

fastfetch
