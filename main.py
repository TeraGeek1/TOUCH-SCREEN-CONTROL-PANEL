from tkinter import *
from tkinter import ttk
from animated_dial import Dial
import threading as thrd


window = Tk()
window.title("Dial Demo")
window.minsize(480, 400)
window.config(padx=20, pady=20, background="#202020")

#### WIDGETS ####
dial1 = Dial(window)
dial1.move_to(100)
dial2 = Dial(window, start=-100, end=100)
dial2.move_to(0)

#### FRAMES ####


#### LAYOUT ####
dial1.pack(side="left", pady=20)
dial2.pack(side="left", pady=20)


window.mainloop()
