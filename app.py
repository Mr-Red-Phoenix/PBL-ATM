import tkinter as tk
from frontend.login import login_screen
from backend.accounts import add_account

def add_default_accounts():
    default_users = [
        ("parth", "1234"),
        ("gyan", "1111"),
        ("vansh", "2222"),
        ("bikki", "3333")
    ]
    for username, pin in default_users:
        add_account(username, pin)

def main():
    add_default_accounts()
    root = tk.Tk()
    root.geometry("300x200")
    login_screen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
