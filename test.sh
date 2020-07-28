#!/usr/bin/env bash

killall ulauncher | true
cp -r . ~/.local/share/ulauncher/extensions/ulauncher-random-generator
ulauncher -v