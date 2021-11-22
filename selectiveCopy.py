#! usr/bin/python3

# selectiveCopy.py - this script walk through a folder tree and
# searches for files with a certain file extension. Then copy these
# files to a new folder

import os
import shutil
from pathlib import Path


# Create regex that matches files with certain file extension
def copy_files(folder):
    folder = Path(os.path.abspath(folder))
    
    for folder_name, subfolders, filenames in os.walk(folder):
        for file in Path(folder_name).glob('*.txt'):
            shutil.copy(file, Path.home() / 'new_delicious')
            

copy_files('/home/artem/delicious')
