from tkinter import *
from Main import *
import keyboard
import pyperclip
from config import *
class MainWindow:
    def button_ok_listener(self,event):
        url =self.text_name.get('1.0',END)
        url = converUrl(url)
        list =getImageUrls(url)
        if list is not None:
            self.text_sex.delete('1.0',END)
            self.text_sex.insert(INSERT,list[-1:])
            pyperclip.copy("".join(list[-1:]))
    def button_save_listener(self,event):
        url =self.text_name.get('1.0',END)
        dict ={"LastUrl":url}
        updateConfig(dict)
    def Listener(self):
        url = self.text_name.get('1.0', END)
        url = converUrl(url)
        list = getImageUrls(url)
        if list is not None:
            self.text_sex.delete('1.0', END)
            self.text_sex.insert(INSERT, list[-1:])
            pyperclip.copy("".join(list[-1:]))
    def __init__(self):
        self.frame = Tk()

        self.label_name = Label(self.frame, text="youdao_url:")
        self.label_sex = Label(self.frame, text="image_url:")


        self.text_name = Text(self.frame, height="1", width=30)
        if getRecURL() is not None:
            self.text_name.insert("1.0", getRecURL())
        self.text_sex = Text(self.frame, height="1", width=30)

        self.label_name.grid(row=0, column=0)
        self.label_sex.grid(row=1, column=0)

        self.button_save = Button(self.frame,text ="save" ,width=10)
        self.button_ok = Button(self.frame, text="ok", width=10)

        self.text_name.grid(row=0, column=1)
        self.text_sex.grid(row=1, column=1)

        self.button_save.grid(row=0,column=2,padx=10)
        self.button_ok.grid(row=1, column=2,padx=10)

        self.button_ok.bind("<ButtonRelease-1>",self.button_ok_listener)
        self.button_save.bind("<ButtonRelease-1>",self.button_save_listener)
        keyboard.add_hotkey('ctrl+shift+a', self.Listener)
        self.frame.mainloop()


frame = MainWindow()