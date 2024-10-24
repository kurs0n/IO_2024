import os
import subprocess

def convert_to_mov(): 
    for fn in os.listdir('.'):
        if os.path.isfile(fn):
            if fn.endswith(".mp4"):
                print("mp4 file found: " + fn)
                p = subprocess.run(
                    ["ffmpeg",
                    "-i", fn,
                    "-n",
                    "-acodec", "copy",
                    "-vcodec", "copy",
                    "-f", "mov", fn[:-4] + ".mov"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=False)
                if p.returncode == 0:
                    os.remove(fn)
                    print("Converted " + fn)
                else:
                    print("Skipped   " + fn)
                    
def convert_to_mp4():
     for fn in os.listdir('.'):
        if os.path.isfile(fn):
            if fn.endswith(".mov"):
                print("mov file found: " + fn)
                p = subprocess.run(
                    ["ffmpeg",
                    "-i", fn,
                    "-n",
                    "-acodec", "aac",
                    "-vcodec", "h264",
                    "-f", "mp4", fn[:-4] + ".mp4"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=False)
                if p.returncode == 0:
                    os.remove(fn)
                    print("Converted " + fn)
                else:
                    print("Skipped   " + fn)