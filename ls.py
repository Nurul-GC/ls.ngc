"""
Copyright (c) [2023], [Nurul-GC]
All rights reserved.
"""

from os import curdir, listdir, path
from pprint import pp


def getfolderlist(_item):
    folderlist = []
    for item in _item:
        if path.isdir(item):
            folderlist.append(item)
    return folderlist


def getfilelist(_item):
    filelist = []
    for item in _item:
        if path.isfile(item):
            filelist.append(item)
    return filelist


ls = listdir

if __name__ == '__main__':
    print("\n\033[01;32m[ FOLDERS ]")
    for folder in getfolderlist(ls(curdir)):
        print(f"-> {folder}")
    print("\n\033[01;33m[ FILES ]")
    for file in getfilelist(ls(curdir)):
        print(f"-> {file}")
