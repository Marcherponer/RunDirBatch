import os
import subprocess

def main():
    directory = "/mnt/media_hdd/Media/anim/You're Under Arrest/"
    presets = ['Fast 480p30', 'Fast 576p25', 'Fast 720p30', 'Fast 1080p30', 'HQ 480p30 Surround', 'HQ 576p25 Surround', 'HQ 720p30 Surround', 'HQ 1080p30 Surround']
    
    for files in sorted(os.listdir(directory)):
        if files.split('.')[-1] == 'mkv':
            print('processing ' + files)
            newName = files.split('.')
            newName[-2] = newName[-2] + '_compressed'
            newName = ".".join(newName)
            subprocess.run(["taskset", "-c", "1,2,3", "HandBrakeCLI",  "--preset=\"Fast 480p30\"", "-a", "\"1,2,3,4,5,6\"", "--aencoder", "copy:dtshd", "-s", "\"1,2,3,4,5,6\"", "-i", "\"" + directory + files + "\"", "-o", "\"" + directory + newName + "\""])

    print('done')
    return None


main()
