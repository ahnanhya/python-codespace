import tkinter as tk
from tkinter import messagebox

def file_open():
    messagebox.showinfo("File", "Open File clicked")

def file_exit():
    root.quit()

def edit_cut():
    messagebox.showinfo("Edit", "Cut clicked")

def help_about():
    messagebox.showinfo("Help", "This is a help message")

root = tk.Tk()
root.title("Menu Bar Example")

# Create Menu Bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Exit", command=file_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=edit_cut)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=help_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Display menu bar
root.config(menu=menu_bar)

root.mainloop()
