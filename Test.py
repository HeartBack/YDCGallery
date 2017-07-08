import keyboard
import pyperclip
import os
from tkinter import *
import subprocess,os
def exe(pyfile,dest="",creator=r"E:\software\Python36\Scripts\pyinstaller.exe",ico=r"C:\Users\Yi\Desktop\ico.ico",noconsole=False):
    insert=""
    if dest:insert+='--distpath="{}"'.format(dest)
    else: insert+='--distpath="./"'.format(os.path.split(pyfile)[0])
    if ico: insert+=' --icon="{}" '.format(ico)
    if noconsole: insert+=' --noconsole '

    print(insert)
    runstring='"{creator}" "{pyfile}" {insert} -F'.format(**locals())
    subprocess.check_output(runstring)
def delet_file(dir):
    for f in os.listdir(dir):
        if f.endswith(".toc"):
            os.remove(os.path.join(dir,f))
delet_file("C:\\Users\\Yi\\Desktop\\")
exe(pyfile='F:\\Python\\YDCGallery\\UI.py',dest='C:\\Users\\Yi\\Desktop\\UI',noconsole=True)