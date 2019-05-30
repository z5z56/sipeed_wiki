#!python
#coding:utf-8

import os


######### change css of k210/board/index.html ################
def change_page_inner_width(file, width):
    if not os.path.exists(f_en_path):
        return
    f = open(file)
    content = f.read()
    content = content.replace('<div class="page-inner">', '<div class="page-inner" style="max-width:100%; margin-left:50px;">')
    f.close()
    f = open(file, "w")
    f.write(content)
    f.close()

f_en_path = None
f_zh_path = None
if os.path.exists("_book"):
    f_en_path = os.getcwd()+"/_book/en/maix/board/index.html"
    f_zh_path = os.getcwd()+"/_book/zh/maix/board/index.html"
elif os.path.exists("build"):
    f_en_path = os.getcwd()+"/build/en/maix/board/index.html"
    f_zh_path = os.getcwd()+"/build/zh/maix/board/index.html"


change_page_inner_width(f_en_path, 1240)
change_page_inner_width(f_zh_path, 1240)

###############################################################