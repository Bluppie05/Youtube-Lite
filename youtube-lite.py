import os
import platform
import glob
import time
from multiprocessing import Process

os.system("firefox https://youtube.com/")

system = platform.system()
link = input("Video link: ")

if system == 'Windows':
    print("Windows is exprerimental and never tested, If any buggs ocur please report them.")
    os.system("dl.exe -f 18 " + link)
    
    list_of_files = glob.glob('*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    video = str(latest_file)
    os.rename(video, "video.mp4")

    os.system("start video.mp4")
    time.sleep(3)
    os.system("del video.mp4")

elif system == 'Linux':
    os.system("youtube-dl -f 18 " + link)
    
    list_of_files = glob.glob('*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    video = str(latest_file)
    os.rename(video, "video.mp4")

    os.system("mpv video.mp4")
    time.sleep(3)
    os.system("rm video.mp4")

elif system == 'Macos':
    print("Macos is exprerimental and never tested, If any buggs ocur please report them.")
    os.system("youtube-dl -f 18 " + link)
    
    list_of_files = glob.glob('*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    video = str(latest_file)
    os.rename(video, "video.mp4")

    os.system("mpv video.mp4")
    time.sleep(3)
    os.system("rm video.mp4")



