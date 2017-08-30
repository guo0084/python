#!/usr/bin/python3.5

import sys
import shelve
from tkinter import *
from tkinter.messagebox import showerror

sys.path.append('/home/glb/python/chapter1/oop')

from person import *
from  manager import *


shelve_name = '../../oop/people'
field_name=('name', 'age', 'job', 'pay')

def make_widges():
    global entries
    window=Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries={}
    for (ix, label) in enumerate(('key',) + field_name):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=fetch_record).pack(side=LEFT)
    Button(window, text='update', command=update_record).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window

def fetch_record():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title='Error', message='No such key:%s' % key)
    else:
        for field in field_name:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def update_record():
    key = entries['key'].get()
    print(key)
    if key in db:
        record = db[key]
    else:
        record = person(name='?', age='?')

    print(record)
    for field in field_name:
        txt = entries[field].get()
        print(txt)
        setattr(record, field, eval(txt))
    db[key] = record

db = shelve.open(shelve_name)
window = make_widges()
window.mainloop()
db.close()
