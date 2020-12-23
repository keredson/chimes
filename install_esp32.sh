set -e
set -x

TTY=/dev/ttyUSB0
SPEED=115200

cd deps
ls *.py | xargs -l ampy -p "$TTY" -b "$SPEED" put
cd ..

ampy -p "$TTY" -b "$SPEED" put mido
ampy -p "$TTY" -b "$SPEED" put main.py

