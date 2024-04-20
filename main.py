from tkinter import *
from tkinter import ttk
from animated_dial import Dial
from menu import Menu
import threading as thrd


window = Tk()
window.title("Dial Demo")
window.minsize(800, 480)
window.config(background="#202020")

#### FRAMES ####
menu = Menu(window)

#### WIDGETS ####
left_dial = Dial(window)
right_dial = Dial(window, start=-100, end=100, minor_divisions=5)


#### Gid config ####
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=10)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=10)
window.columnconfigure(4, weight=1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=25)
window.rowconfigure(2, weight=1)

#### LAYOUT ####
menu.tkraise(left_dial)
left_dial.grid(row=1, column=1)
right_dial.grid(row=1, column=3)


window.mainloop()
