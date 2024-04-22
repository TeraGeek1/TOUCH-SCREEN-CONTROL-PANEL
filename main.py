from tkinter import *
from tkinter import ttk
from animated_dial import Dial
from menu import CustomMenu
import threading as thrd


def save_config():
    if set_left.get() != "":
        left_dial.move_to(int(set_left.get()))
    if set_right.get() != "":
        right_dial.move_to(int(set_right.get()))


window = Tk()
window.title("Dial Demo")
# window.attributes("-fullscreen", True)
window.minsize(800, 480)
window.config(background="#202020")


#### WIDGETS ####
left_dial = Dial(window, start=-100, end=100, minor_divisions=5)
right_dial = Dial(window, start=-100, end=100, minor_divisions=5)

# menu
menu = CustomMenu(window)
menu.columnconfigure(0, weight=2)
for i in range(1, 4):
    menu.columnconfigure(i, weight=1)

left_label = Label(menu, text="Set left Dial")
set_left = Entry(menu)

right_label = Label(menu, text="set right Dial")
set_right = Entry(menu)


menu.add_category(
    "Calibrate",
    [Button(menu, text="Save", command=save_config), 0.88, 0.01],
    left_label,
    set_left,
    right_label,
    set_right,
)


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

left_label.grid(row=1, column=1)
set_left.grid(row=2, column=1)

right_label.grid(row=1, column=3)
set_right.grid(row=2, column=3)


window.mainloop()
