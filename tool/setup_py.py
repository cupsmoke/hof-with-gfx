import re
import os
import io
import os.path

#
import subprocess
print('启动照片强化: 1\n启动gfx生成器: 2')
corenum = input('请输入')
if corenum == '1':
    # 启动
    print('启动照片强化')
    path = 'E:/download/github download/pywork'
    pypath = os.path.join(path,'en_image_2.py')
    subprocess.run(['python', pypath])
elif corenum == '2':
    # 启动
    print('启动gfx生成器')
    path = 'E:/download/github download/hof-with-gfx/tool'
    pypath = os.path.join(path,'from png to gfx-portrait.py')
    subprocess.run(['python', pypath])
    pypath = os.path.join(path,'from png to gfx-idea.py')
    subprocess.run(['python', pypath])
    pypath = os.path.join(path,'from png to gfx-focus.py')
    subprocess.run(['python', pypath])
    pypath = os.path.join(path,'from png to gfx-advisor.py')
    subprocess.run(['python', pypath])
    pypath = os.path.join(path,'from png to gfx-event.py')
    subprocess.run(['python', pypath])
# subprocess.run(['python', 'from png to gfx-event.py'])
# print(path1)