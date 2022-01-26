#!/bin/bash
cd /home/ooz3/Note

wc -l  ytdl.txt | cut -c 1,2 > numero1.txt

read -r NUM < numero.txt
read -r NUM1 < numero1.txt

let "NUM=$NUM1-$NUM+1"

sed -n "$NUM","$NUM1"p  ytdl.txt > ytdl1.txt

#grep youtube.com /run/user/1001/clipmenu.6.ooz3/line_cache |cut -c 20- > Note/ytdl.txt

sleep 2

youtube-dl -a ytdl1.txt -x --audio-format 'mp3' -o ~/Music/'%(album)s-%(title)s.%(ext)s'

echo "0" > numero.txt

