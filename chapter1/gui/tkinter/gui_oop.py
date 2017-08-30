#!/usr/bin/python3.5

from tkinter import *
from tkinter.messagebox import showinfo

class my_gui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command = self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed')

class custom_gui(my_gui):
    def reply(self):
        showinfo(title='popup', message = 'Ouch')

def replay(name):
    showinfo(title='Reply', message='Hello %s!' % name)
        
if __name__ == '__main__':

    top = Tk()
    top.title('Echo')
    #top.iconbitmap()
    Label(top, text='please entry your name:').pack(side=TOP)
    ent = Entry(top)
    ent.pack()
    btn = Button(top, text='Submit', command=(lambda: replay(ent.get())))
    btn.pack()
    top.mainloop()
    
    #mainwin = Tk()
    #Label(mainwin, text=__name__).pack(side=RIGHT)
    #pp = Toplevel()
    #Label(pp, text='Attach').pack(side=LEFT)
    #custom_gui(pp).pack(side=RIGHT)
    #mainwin.mainloop()

    
    #window = my_gui()
    #window.pack()
    #window.mainloop()

    
