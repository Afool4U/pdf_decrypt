# -*- coding = utf-8 -*-
# @Time: 2022/9/24 14:57
# @Author: Afool4U
# @File: 一键解密PDF权限.py
# @Software: PyCharm

from ctypes import windll
from os import path
from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
from tkinter import Tk, Button
import tkinter.filedialog
from tkinter.messagebox import showinfo
from pikepdf import open


def pdf_Crack(startFile, endFile):
    with open(startFile) as pdf:
        pdf.save(endFile)
        return endFile


def get_desktop():
    key = OpenKey(HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return QueryValueEx(key, "Desktop")[0]


def over():
    showinfo("信息", "解密文件已输出至桌面！")


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    windll.shcore.SetProcessDpiAwareness(1)
    # 调用api获得当前的缩放因子
    ScaleFactor = windll.shcore.GetScaleFactorForDevice(0)
    # 设置缩放因子
    root.tk.call('tk', 'scaling', ScaleFactor / 75)
    b = Button(root, text='测试弹窗')
    b.pack()
    b.bind('<Button-1>', over)
    default_dir = get_desktop()
    image_paths = tkinter.filedialog.askopenfilenames(title=u'请选择需要处理的文件，可选择多个：',
                                                      initialdir=(path.expanduser(default_dir)),
                                                      filetypes=(("pdf文件", "*.pdf"),))
    for image_path in image_paths:
        pdf_Crack(image_path, default_dir + '\\' + path.basename(image_path) + '_已解密.pdf')
    if len(image_paths) != 0:
        over()

# pyinstaller  -i logo.ico -F -w --copy-metadata pikepdf 一键解密PDF权限.py
