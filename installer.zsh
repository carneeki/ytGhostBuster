#!/usr/bin/zsh

SCRIPTDIR=~/.local/bin/
TIMERSDIR=~/.config/systemd/user/
sedstring="s/REPLACEME/$(whoami)/g"

mkdir -p $SCRIPTDIR
cp ytGhostBuster.py $SCRIPTDIR/ytGhostBuster.py


mkdir -p $TIMERSDIR
cp ytGhostBuster.service $TIMERSDIR/ytGhostBuster.service
sed -i $sedstring $TIMERSDIR/ytGhostBuster.service
cp ytGhostBuster.timer $TIMERSDIR/ytGhostBuster.timer


systemctl --user enable ytGhostBuster.service
systemctl --user enable ytGhostBuster.timer
systemctl --user start ytGhostBuster.service
systemctl --user start ytGhostBuster.timer
