import re
import os
import io
import os.path

def getDir(path):
    taglist = []
    taglist1 = os.listdir(path)
    for tag in taglist1:
        path1 = path + tag
        if os.path.isdir(path1):
            taglist.append(tag)
    return taglist

def getPngName(tagpath):
    taglist = os.listdir(tagpath)
    return taglist
# print(path1)