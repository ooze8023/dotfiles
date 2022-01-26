#!/bin/zsh
hacksaw -f %i>/home/ooz3/Immagini/screenshot/geometry.txt
cd /home/ooz3/Immagini/screenshot

while IFS= read -r line; do a="$line "; done < geometry.txt

DATE=$(date +%Y%m%d)
filename="${DATE}.png"
num=0
while [ -f $filename ]; do
    num=$(( $num + 1 ))
    filename="${DATE}-${num}.png"
done
touch $filename

VAR1=" shotgun -i "
VAR3="/home/ooz3/Immagini/screenshot/"
VAR2="$VAR1$a$filename"
      printf "$VAR2">shot1.sh
sleep 1 && ./shot1.sh










