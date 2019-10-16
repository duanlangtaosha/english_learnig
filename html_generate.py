# -*- coding: utf-8 -*-

import sys
import os
import shutil
from multiprocessing import Process

'''
    必须要先安装好相应的latex发行包，然后添加到环境变量
'''

CURRENT_DIR = os.path.split(__file__)[0]
print(CURRENT_DIR)

def run_create_html():
    # 创建网页
    os.system("sphinx-build -M {} {} {}".format('html', os.path.join(CURRENT_DIR, 'source'), os.path.join(CURRENT_DIR, 'build')))
    
    print('html generate ok!')

def run_create_pdf():
    # 生成tex文件
    tex_file = ''
    os.system("sphinx-build -M {} {} {}".format('latex', os.path.join(CURRENT_DIR, 'source'), os.path.join(CURRENT_DIR, 'build')))
    objdir = os.path.join(CURRENT_DIR, 'build', 'latex')
    files = os.listdir(objdir)
    os.chdir(objdir)

    for file in files:
        if file.endswith(".tex"):
            tex_file = file
            break

    # 心须执行两次,第二次生成目录和参考文献
    os.system("xelatex -interaction nonstopmode -f {}".format(tex_file))
    os.system("xelatex -interaction nonstopmode -f {}".format(tex_file))

    files = os.listdir(objdir)
    for file in files:
        if file.endswith(".pdf"):
            dst = shutil.copy(os.path.join(objdir, file), os.path.join(objdir, '..', file))
            print(dst)
            print('generate ok!!!!!!!!!!!!!')
            break
    print('pdf generate ok!')




if __name__ == "__main__":

    p_html = Process(target = run_create_html)
    #p_pdf = Process(target = run_create_pdf)
    p_html.start()
    #p_pdf.start()

    p_html.join()
    #p_pdf.join()
    print("the build ok!")
