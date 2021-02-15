# Author: SPARSH GUPTA
# Program to copy Windows Lockscreen wallpaper from default to user defined location

"""
Windows Spotlight - Windows 10's lock screen features a periodic rotation of some really cool wallpapers.
If we want to save the images you find, here’s where to find them on your hard drive.
"""

import shutil
import os

source = r"C:\Users\Administrator\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy" \
         r"\LocalState\Assets "
destination = r"D:\GIJoe\Personal\Wallpapers\Windows Lockscreen"

'''
If we try to create a directory that is already present, you will get FileExistsError. 
So we must check if the directory is already present or not and then skip it
'''

'''
shutil copy works only on absolute path. Else it will give permission denied error.
'''


def copy_windows_spotlight_wallpapers():
    for file in os.listdir(source):
        source_file_path = os.path.join(source, file)
        destination_file_path = os.path.join(destination, file) + '.jpeg'
        shutil.copy(source_file_path, destination_file_path)


if __name__ == "__main__":
    copy_windows_spotlight_wallpapers()
    print("All wallpapers copied successfully")
