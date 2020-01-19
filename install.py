#!/usr/bin/env python3

import platform
import os

system = platform.system()

if system == 'Windows':
        print("Windows is exprerimental and never tested, If any buggs ocur please report them.")
        os.system("curl https://youtube-dl.org/downloads/latest/youtube-dl.exe -O dl.exe")

elif system == 'Macos':
    print("Macos is exprerimental and never tested, If any buggs ocur please report them.")
    os.system("sudo curl https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl")

    print("You'll need to install MPV to run this program: https://mpv.io/installation/")
    os.system("safari https://mpv.io/installation/")

elif system == 'Linux':
    os.system("sudo apt install youtube-dl")
    os.system("sudo apt install mpv")
    os.system("sudo apt install firefox")
    print("Done! you can now start youtube-lite")

else:
    print("Error: System not supported, Your system is coming soon.")