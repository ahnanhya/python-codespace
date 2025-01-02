import tkinter as tk

def show_choice():
    choice = "Radio Button Selection: " + var.get() + "\n"
    choice += "Checkbox Selection: " + str(var_check.get())
    label.config(text=choice)

root = tk.Tk()
root.title("Radio Buttons and Checkboxes")

# Radio Buttons
var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
radio1.pack()
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
radio2.pack()

# Checkbox
var_check = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Check me", variable=var_check)
checkbox.pack()

# Show button
button = tk.Button(root, text="Show Selection", command=show_choice)
button.pack()

# Label for showing selections
label = tk.Label(root, text="")
label.pack()

root.mainloop()
