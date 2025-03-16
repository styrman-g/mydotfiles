#!/usr/bin/env bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

run "picom"
run "nm-applet"
run "nitrogen --restore"
run "syncthingtray"
run "dunst"
run "udiskie"
run "signal-desktop"
