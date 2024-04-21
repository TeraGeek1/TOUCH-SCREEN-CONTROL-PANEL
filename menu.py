from tkinter import *
from tkinter import Misc, ttk
import sys


class CustomMenu(ttk.Frame):
    def __init__(self, master: Misc | None = None, relheight=1, relwidth=0.4):
        super().__init__(master)

        # data holders
        self.categories = {}  # used to store menu items and there sub items

        # visual
        self.menu_button = Button(master, text="Menu", command=self.show_menu)
        self.close_menu_button = Button(self, text="Close", command=self.hide_menu)
        self.exit_button = Button(self, text="Exit", command=self.exit_app)

        # Settings
        self.aboveThis = None
        self.relheight = relheight
        self.relwidth = relwidth

        # Place menu button
        self.menu_button.place(relx=0.01, rely=0.01)

    def add_category(self, cat_name: str, *args):
        self.categories[cat_name] = {}
        self.categories[cat_name]["children"] = args
        self.categories[cat_name]["parent"] = Button(
            self,
            text=cat_name,
            command=lambda cat_name=cat_name: self.enter_category(cat_name),
        )

    def enter_category(self, cat_name):
        self.hide_menu()
        self.place(relwidth=self.relwidth, relheight=self.relheight)
        self.menu_button.place_forget()

        row_idx = 0
        for child in self.categories[cat_name]["children"]:
            child: Widget
            if type(child) != list:
                child.grid(row=row_idx, column=0)
                continue
            column_idx = 0
            for c in child:
                c.grid(row=row_idx, column=column_idx)
                column_idx += 1
            row_idx += 1

    def show_menu(self):
        self.place(relwidth=self.relwidth, relheight=self.relheight)

        y_pos = 0.08
        for category in self.categories:
            self.categories[category]["parent"].place(relx=0.01, rely=y_pos)
            y_pos += 0.06

        self.menu_button.place_forget()
        self.close_menu_button.place(relx=0.01, rely=0.01)
        self.exit_button.place(relx=0.01, rely=0.95)

    def hide_menu(self):
        self.place_forget()
        self.menu_button.place(relx=0.01, rely=0.01)
        self.close_menu_button.place_forget()

        for category in self.categories:
            self.categories[category]["parent"].place_forget()
            for child in self.categories[category]["children"]:
                if type(child) != list:
                    child.place_forget()
                else:
                    for c in child:
                        c.place_forget()

    def exit_app(self):
        sys.exit()
