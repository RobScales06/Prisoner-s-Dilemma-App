#Layout Pallette for tkinter
#Created by Rob Scales
#11-27-2019

from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

def makeButton(window,x,y,name, function):
    btn = Button(window, text=name, command=function)
    btn.grid(column=x, row=y)

def makeWindow(window,name="Window",x=250,y=350):
    window.title(name)
    
    window.geometry(str(x)+'x'+str(y))

def makeCheck(window,x,y,name):
    var = IntVar()
    check = Checkbutton(window, text=name, variable=var)
    check.grid(column=x, row=y)
    return var

def makeLabel(window,x,y,name):
    lblName = Label(window, text=name)
    lblName.grid(column=x, row=y)

def makeImg(window,xPos,yPos,file,width,height): 
    load = Image.open(file)
    load = load.resize((height, width), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render)
    img.image = render
    img.grid(column=xPos, row=yPos)

def makeDropdown(window,x,y,options):
        #Options
    OPTIONS = []
    OPTIONS = options
    OPTIONS.insert(0,options[0])
    varSource = StringVar(window)
    varSource.set(OPTIONS[0]) # default value
    omnSource = OptionMenu(window, varSource, *OPTIONS)
    omnSource.grid(column=x, row=y)
    return varSource
