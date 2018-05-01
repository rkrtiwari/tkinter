#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 09:15:42 2018

@author: ravi
"""

from Tkinter import *
import numpy as np
size = 500

x0 = 20
y0 = 80
x1 = 80
r = 20
xstep = 80
ystep = 40

x = np.random.choice(range(10))
y = np.random.choice(range(1,10))

z = x + y

window = Tk()
canvas = Canvas(window, width = size, height = size)
#canvas.place(x= 0, y = 0)
canvas.pack()

label1 = Label(window, text = x, fg = 'red', bg = 'black', font = "Helvetica 15")
label1.place(x = x0, y = 50)
label2 = Label(window, text = '+', fg = 'red', bg = 'black', font = "Helvetica 15")
label2.place(x = 50, y = 50)
label3 = Label(window, text = y, fg = 'green', bg = 'black', font = "Helvetica 15")
label3.place(x = x1, y = 50)
label4 = Label(window, text = '=', fg = 'red', bg = 'black', font = "Helvetica 15")
label4.place(x = 110, y = 50)
label5 = Label(window, text = z, fg = 'blue', bg = 'black', font = "Helvetica 15")
label5.place(x = 140, y = 50)

#button1 = Button(window, text = ' ', command )


for i in range(x):
    canvas.create_oval(x0, y0 + i*ystep, x0 + r, y0 + i*ystep+ r, fill = 'red')
    window.update()

for i in range(y):
    canvas.create_oval(x1, y0+ i*ystep, x1 + r, y0 +i*ystep+ r, fill = 'green')
    window.update()

window.mainloop()

