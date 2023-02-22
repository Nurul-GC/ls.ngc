"""
BSD 3-Clause License
Copyright (c) [2023], [Nurul-GC]
All rights reserved.
"""

from os import curdir, listdir, path
from pprint import pp
from sys import argv

ls = listdir


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


def gethelp():
    return "[ INFO ]\n\n" \
           "ls.ngc - is an enhaced copy of the `ls` command on Unix terminals, made for windows'users.\n\n" \
           "[ USAGE ]\n" \
           "ls - return all the files and folders into the current directory.\n\n" \
           "[ PARAMETERS ]\n" \
           "-v | --version | \\v - show the info about the program.\n" \
           "-h | --help | \\h - show this intro information.\n\n" \
           "© 2023 Nurul-GC\n" \
           "™ArtesGC Inc.\n"


def getversion():
    return "[ ABOUT ]\n\n" \
           "[NAME] -> ls.ngc\n" \
           "[VERSION] -> v0.1-022023\n" \
           "[LICENSE] -> BSD 3-Clause License\n" \
           "[MAINTAINER] -> © 2023 Nurul-GC\n" \
           "[PUBLISHER] -> ™ArtesGC Inc."


if __name__ == '__main__':
    if len(argv) > 1:
        if argv[1] == ("-v" or "--version" or "\\v"):
            print(f"\033[01;32m{getversion()}")
        elif argv[1] == ("-h" or "--help" or "\\h"):
            print(f"\033[01;32m{gethelp()}")
    else:
        print("\n\033[01;31m[ FOLDERS ]")
        for folder in getfolderlist(ls(curdir)):
            print(f"-> {folder}")
        print("\n\033[01;33m[ FILES ]")
        for file in getfilelist(ls(curdir)):
            print(f"-> {file}")
