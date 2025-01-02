import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Example check (Replace with real validation)
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid credentials")

root = tk.Tk()
root.title("Login Form")

# Username
label_username = tk.Label(root, text="Username")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

# Password
label_password = tk.Label(root, text="Password")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
