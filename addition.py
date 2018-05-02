#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 09:15:42 2018

@author: ravi
"""

from Tkinter import *
import numpy as np
import os
xsize = 2000
ysize = 1000

x0 = 20
y0 = 180
x1 = 220
r = 20
xstep = 80
ystep = 80

correct = 0
wrong = 0


x = np.random.choice(range(1,10))
y = np.random.choice(range(1,10))

z = x + y

window = Tk()
canvas = Canvas(window, width = xsize, height = ysize)
#canvas.place(x= 0, y = 0)
canvas.pack()
label1 = Label(window, text = x, fg = 'red', bg = 'black', font = "Helvetica 60")
label1.place(x = x0, y = 50)
label2 = Label(window, text = '+', fg = 'red', bg = 'black', font = "Helvetica 60")
label2.place(x = 120, y = 50)
label3 = Label(window, text = y, fg = 'green', bg = 'black', font = "Helvetica 60")
label3.place(x = x1, y = 50)
label4 = Label(window, text = '=', fg = 'red', bg = 'black', font = "Helvetica 60")
label4.place(x = 320, y = 50)
text = '         '
label5 = Label(window, text = text, fg = 'red', bg = 'black', font = "Helvetica 60")
label5.place(x = 550, y = 50)

label6 = Label(window, text = correct, fg = 'red', bg = 'black', font = "Helvetica 60")
label6.place(x = 1250, y = 50)

label7 = Label(window, text = wrong, fg = 'red', bg = 'black', font = "Helvetica 60")
label7.place(x = 1350, y = 50)



def click(event):
    global correct
    global wrong
    if data.get() == z:
        text = 'Yey    '
        label5.config(text=text)
        os.system('mplayer -ss 2 -endpos 2 correct.mp3')
        correct +=1
        label6.config(text = correct)
    else:
        text = 'Try Again'
        label5.config(text=text)
        os.system('mplayer -ss 2 -endpos 2 wrong.mp3')
        wrong += 1
        label7.config(text = wrong)
#    label5.config(text=text)
    

data = IntVar()
e = Entry(window, textvariable = data, width = 2, font = "Helvetica 60")
e.place(x = 420, y = 50)
e.bind("<Return>", click)
value = e.get()
  

for i in range(x):
    canvas.create_oval(x0, y0 + i*ystep, x0 + r, y0 + i*ystep+ r, fill = 'red')
    window.update()

for i in range(y):
    canvas.create_oval(x1, y0+ i*ystep, x1 + r, y0 +i*ystep+ r, fill = 'green')
    window.update()


def press():
    global x
    global y
    global z
    global correct
    global wrong
    x = np.random.choice(range(1,10))
    y = np.random.choice(range(1,10))
    z = x + y
    total += 1
    label1.config(text=x)
    label3.config(text=y)
    
    text = '          '
    label5.config(text = text)
    
    canvas.delete('all')
    for i in range(x):
        canvas.create_oval(x0, y0 + i*ystep, x0 + r, y0 + i*ystep+ r, fill = 'red')
        window.update()
        
    for i in range(y):
        canvas.create_oval(x1, y0+ i*ystep, x1 + r, y0 +i*ystep+ r, fill = 'green')
        window.update()
        

b1 = Button(window, text = "new sum?", command = press, font = "Helvetica 30")
b1.place(x=950, y=60)


window.mainloop()

