import re
import os
import io
import os.path
import shutil
# 路径识别
import core

# 需要的输入：
# 路径 TAG

# TAG = input('请输入TAG：').upper()

def outpuGfx(text):
    global interfacePath
    global gfxfilename
    pngpath = 'gfx/interface/ideologies/'
    txtfile = open(gfxfilename , 'w',encoding='UTF-8')
    # spriteTypes = {
    txtfile.write('spriteTypes = {\n')
    for txt in text:
        txt = re.sub('.png','',txt).strip()
        pngfullname = '\t\ttexturefile = \"'+pngpath+txt+'.png\"\n'
        pngfullgfxname = '\t\tname = \"GFX_ideology_'+txt + '\"\n'
        txtfile.write('\tSpriteType = {\n')
        txtfile.write(pngfullgfxname)
        txtfile.write(pngfullname)
        txtfile.write('\t}\n')
    txtfile.write('}\n')
    txtfile.close()
    print("ideo.gfx文件已输出")
pngpathfirst = '../gfx/interface/ideologies/'

input('')
interfacePath = '../interface/ideology/'
if os.path.exists(interfacePath):
    shutil.rmtree(interfacePath)
if not os.path.exists(interfacePath):
    os.makedirs(interfacePath)

gfxfilename = interfacePath + 'ideology_fate.gfx'
pnglist = core.getPngName(pngpathfirst)
outpuGfx(pnglist)

# for tag in taglist:
#     print(tag)
print('共有',len(pnglist),'个ideo图标')
#
# input('')
