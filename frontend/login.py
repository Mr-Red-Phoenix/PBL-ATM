import tkinter as tk
from tkinter import messagebox
from backend.auth import authenticate
from frontend.main_menu import open_main_menu

def login_screen(root):
    root.title("ATM Login")
    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Username").grid(row=0, column=0)
    tk.Label(frame, text="PIN").grid(row=1, column=0)

    username = tk.Entry(frame)
    pin = tk.Entry(frame, show="*")

    username.grid(row=0, column=1)
    pin.grid(row=1, column=1)

    def attempt_login():
        user = username.get()
        code = pin.get()
        if authenticate(user, code):
            frame.destroy()
            open_main_menu(root, user)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    tk.Button(frame, text="Login", command=attempt_login).grid(row=2, column=1, pady=10)
