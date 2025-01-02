import tkinter as tk

def change_color(event):
    color = dropdown_var.get()
    root.config(bg=color)

root = tk.Tk()
root.title("Color Changer")

# Dropdown menu for colors
colors = ["Red", "Green", "Blue", "Yellow", "Pink"]
dropdown_var = tk.StringVar()
dropdown_var.set(colors[0])  # Set default value

dropdown_menu = tk.OptionMenu(root, dropdown_var, *colors)
dropdown_menu.pack()

# Bind event to change color
dropdown_menu.bind("<Configure>", change_color)

root.mainloop()
