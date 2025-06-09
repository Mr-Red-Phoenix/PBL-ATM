import tkinter as tk
from frontend.operations import open_operations

def open_main_menu(root, username):
    root.title("ATM Main Menu")
    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text=f"Welcome, {username}").pack(pady=10)

    options = ["Check Balance", "Deposit", "Withdraw", "Transfer", "Other Services"]
    for op in options:
        tk.Button(frame, text=op, width=20, command=lambda o=op: open_operations(root, username, o)).pack(pady=5)
