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
    global TAG
    pngpath = 'gfx/interface/advisor/' + TAG
    txtfile = open(interfacePath + 'advisor_'+ TAG + '.gfx' , 'w',encoding='UTF-8')
    # spriteTypes = {
    txtfile.write('spriteTypes = {\n')
    for txt in text:
        txt = re.sub('.png','',txt).strip()
        pngfullname = '\t\ttexturefile = \"'+pngpath+'/'+txt+'.png\"\n'
        pngfullgfxname = '\t\tname = \"GFX_idea_'+txt + '\"\n'
        txtfile.write('\tSpriteType = {\n')
        txtfile.write(pngfullgfxname)
        txtfile.write(pngfullname)
        txtfile.write('\t}\n')
    txtfile.write('}\n')
    txtfile.close()
    print(TAG+"_advisor.gfx文件已输出")
pngpathfirst = '../gfx/interface/advisor/'
taglist = core.getDir(pngpathfirst)
print('将生成以下tag顾问的gfx文件')
print(taglist)
input('')
interfacePath = '../interface/advisor/'
if os.path.exists(interfacePath):
    shutil.rmtree(interfacePath)
if not os.path.exists(interfacePath):
    os.makedirs(interfacePath)
for TAG in taglist:
    pngpath = os.path.join(pngpathfirst,TAG)
    gfxfilename = interfacePath + 'advisor_' + TAG + '.gfx'
    pnglist = core.getPngName(pngpath)
    outpuGfx(pnglist)

    # for tag in taglist:
    #     print(tag)
    print(TAG,'共有',len(pnglist),'个图标')
#
# input('')
