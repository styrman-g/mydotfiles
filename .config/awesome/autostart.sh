#!/usr/bin/env bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

run "lxsession"
run "picom"
run "nm-applet"
run "volumeicon"
run "nitrogen --restore"
run "syncthingtray"
run "dunst"
run "udiskie"
