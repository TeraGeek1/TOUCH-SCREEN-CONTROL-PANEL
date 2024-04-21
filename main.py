from tkinter import *
from tkinter import ttk
from animated_dial import Dial
from menu import CustomMenu
import threading as thrd


window = Tk()
window.title("Dial Demo")
window.attributes("-fullscreen", True)
window.minsize(800, 480)
window.config(background="#202020")


#### WIDGETS ####
left_dial = Dial(window)
right_dial = Dial(window, start=-100, end=100, minor_divisions=5)

# menu
menu = CustomMenu(window)
menu.add_category(
    "Settings", Button(menu, text="Settings work"), Button(menu, text="Good job")
)
menu.add_category(
    "Calibrate", Button(menu, text="Works"), Button(menu, text="Good job")
)

menu.add_category("test", [Entry(menu), Button(menu, text="Test works")])


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
left_dial.grid(row=1, column=1)
right_dial.grid(row=1, column=3)

# menu
menu.tkraise(left_dial)


window.mainloop()
