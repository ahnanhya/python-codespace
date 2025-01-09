import tkinter as tk
from tkinter import messagebox

# Function to handle selection from the listbox
def on_select(event):
    # Get the selected item
    selected_item = listbox.get(listbox.curselection())
    # Display selected item
    messagebox.showinfo("Selected Item", f"You selected: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("Listbox Selection Example")
root.geometry("300x250")  # Set the size of the window

# List of items to display
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

# Create a Listbox widget
listbox = tk.Listbox(root, height=6, selectmode=tk.SINGLE)
listbox.pack(pady=20)

# Insert the items into the Listbox
for item in items:
    listbox.insert(tk.END, item)

# Bind the selection event to the on_select function
listbox.bind("<<ListboxSelect>>", on_select)

# Run the main loop
root.mainloop()
