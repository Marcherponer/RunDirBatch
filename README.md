# RunDirBatch
Run command for everything in directory

didn't work at all, just use this command:
for i in ./*; do HandBrakeCLI --preset="Fast 480p30" --all-subtitles --all-audio -i "$i" -o comp/"$i"; done
