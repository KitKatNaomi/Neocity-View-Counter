@echo off
convert -size 60x20 xc:pink -fill white -pointsize 15 -gravity center -draw "text 0,0 '%1'" count.jpg