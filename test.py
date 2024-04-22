import tkinter as tk


def toggle():
    if btn1.winfo_manager() == "grid":
        btn1.grid_remove()
    else:
        btn1.grid()

    if btn3.winfo_manager() == "place":
        btn3.place_forget()
    else:
        btn3.place()


root = tk.Tk()

btn1 = tk.Button(root, text="Toggle Grid", command=toggle)


# btn2 = tk.Button(root, text="Toggle Pack", command=toggle_pack)
# btn2.pack()

btn3 = tk.Button(root, text="Toggle Place", command=toggle)
btn3.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
