import os
import subprocess

def main():
    directory = r"/mnt/media_hdd/Media/anim/You're Under Arrest"
    presets = ['Fast 480p30', 'Fast 576p25', 'Fast 720p30', 'Fast 1080p30', 'HQ 480p30 Surround', 'HQ 576p25 Surround', 'HQ 720p30 Surround', 'HQ 1080p30 Surround']

    for files in sorted(os.listdir(directory)):
        print('processing ' + files)
        newName = files.split('.')
        newName = newName[-2] + '_compressed'
        newName = ".".join(newName)
        command = "taskset -c 1,2,3 HandBrakeCLI --preset=\"" + preset[0] + "\" -a \"1,2,3,4,5,6\" --aencoder copy:dtshd -s \"1,2,3,4,5,6\" -i \'" + files + "\' -o '" + newName + "'"
        subprocess.run()
    return None


main()
