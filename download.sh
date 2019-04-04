#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    youtube-dl -o '%(title)s.%(ext)s' -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 --no-check-certificate $line
done < "$1"

