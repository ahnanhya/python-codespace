import tkinter as tk

def display_message():
    label.config(text="Hello, World!")

root = tk.Tk()
root.title("Hello World App")

# Create a label
label = tk.Label(root, text="")
label.pack()

# Create a button
button = tk.Button(root, text="Click Me", command=display_message)
button.pack()

root.mainloop()
