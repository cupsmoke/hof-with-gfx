import re
import os
import io
import os.path
import shutil

def getDir(path):
    taglist = []
    taglist1 = os.listdir(path)
    for tag in taglist1:
        path1 = os.path.join(path,tag)
        if os.path.isdir(path1):
            taglist.append(tag)
    return taglist

def getPngName(tagpath):
    taglist = os.listdir(tagpath)
    return taglist


pngpathfirst = '../gfx/leaders'
taglist = getDir(pngpathfirst)
print('将修改以下tag领袖头像的文件名')
print(taglist)
input('')
N = 0
interfacePath = '../interface/portrait'
if os.path.exists(interfacePath):
    shutil.rmtree(interfacePath)
if not os.path.exists(interfacePath):
    os.makedirs(interfacePath)
for TAG in taglist:
    pngpath = os.path.join(pngpathfirst, TAG)
    pnglist = getPngName(pngpath)
    tag_key = 'Portrait_' + TAG + '_'
    if len(pnglist) > 0:
        print(TAG + ':')
        # print(pnglist)
    for Pname in pnglist:
        oldFullName = os.path.join(pngpath, Pname)
        if tag_key in Pname:
            NewName = Pname
        elif 'Portrait_' in Pname:
            NewName = re.sub('Portrait_', tag_key, Pname)
        else:
            NewName = tag_key + Pname
        NewName = re.sub('\s+', '_', NewName)
        NewName = re.sub('-+', '_', NewName)
        newFullName = os.path.join(pngpath, NewName)
        if NewName != Pname:
            print(Pname + ' -----> ' + NewName)
            N += 1
        os.rename(oldFullName, newFullName)
        # print(oldname)

print('共改变', N ,'个')
# input('')
