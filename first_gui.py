#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 03:37:35 2018

@author: ravi
"""

import os
from Tkinter import *

###############################################################################
# First gui
###############################################################################
root = Tk()
label = Label(root, text = 'I am a label widget')
button = Button(root, text = 'I am a button')
label.pack()
button.pack()
root.mainloop()

###############################################################################
# second gui
###############################################################################
def stopProg(e):
    root.destroy()

def transfertext(e):
    label1.configure(text="Hello World")
   
root=Tk()
root.geometry("330x220+300+300")
button1=Button(root,text="Exit")
button1.pack()
button1.bind('<Button-1>',stopProg)
button2=Button(root,text="Click Me")
button2.pack()
button2.bind('<Button-1>',transfertext)
label1=Label(root,text="nothing to say")
root.mainloop()
canvas = Canvas()
canvas.create_rectangle(230, 10, 290, 60, 
    outline="gray", fill="gray", width=2)

##################################################################################
# circle
###############################################################################

import Tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle



canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
textentry = Entry(canvas)
canvas.create_window(600, 50, window=textentry, height=50, width=1000)

root.wm_title("Circles and Arcs")
root.mainloop()


##############################################################################
# enter a word
###############################################################################
from Tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()


###############################################################################
# draw a circle
###############################################################################
from Tkinter import *
import numpy as np
size = 500

x0 = 100
y0 = 100
r = 20
xstep = 40
ystep = 40

x = np.random.choice(range(10))
y = np.random.choice(range(1,10))

z = x + y

window = Tk()
canvas = Canvas(window, width = size, height = size)
canvas.pack()

label1 = Label(window, text = x, fg = 'red', bg = 'black').pack(side = 'top', padx = 10, pady = 20)
label2 = Label(window, text = y).pack(side = 'top')
label3 = Label(window, text = z).pack(side = 'top')



for i in range(x):
    canvas.create_oval(x0+i*xstep, y0, x0 +i*xstep+ r, y0 + r, fill = 'red')
    window.update()

for i in range(y):
    canvas.create_oval(x0+i*xstep, y0+ystep, x0 +i*xstep+ r, y0 +ystep+ r, fill = 'green')
    window.update()

window.mainloop()







