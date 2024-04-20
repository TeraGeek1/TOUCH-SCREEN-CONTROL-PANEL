from tkinter import *
from tkinter import Misc, ttk


class Menu(ttk.Frame):
    def __init__(self, master: Misc | None = None, relheight=1, relwidth=0.4):
        super().__init__(master)
        self.menu_button = Button(master, text="Menu", command=self.show_menu)
        self.close_menu_button = Button(self, text="Close", command=self.hide_menu)

        # Settings
        self.aboveThis = None
        self.relheight = relheight
        self.relwidth = relwidth

        # Place menu button
        self.menu_button.place(relx=0.01, rely=0.01)

    def show_menu(self):
        self.place(relwidth=self.relwidth, relheight=self.relheight)
        self.menu_button.place_forget()
        self.close_menu_button.place(relx=0.01, rely=0.01)

    def hide_menu(self):
        self.place_forget()
        self.menu_button.place(relx=0.01, rely=0.01)
        self.close_menu_button.place_forget()
