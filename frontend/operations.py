import tkinter as tk
from tkinter import simpledialog, messagebox
from backend.transactions import check_balance, deposit, withdraw, transfer

def open_operations(root, username, operation):
    balance_before = check_balance(username)  # Fetch current balance before operation

    if operation == "Check Balance":
        messagebox.showinfo("Balance", f"Current balance: ${balance_before}")

    elif operation == "Deposit":
        amount = simpledialog.askinteger("Deposit", f"Your balance before deposit: ${balance_before}\nEnter amount:")
        if amount and amount > 0:
            balance_after = deposit(username, amount)
            messagebox.showinfo("Success", f"Deposited ${amount}.\nBalance before deposit: ${balance_before}\nNew balance: ${balance_after}")

    elif operation == "Withdraw":
        amount = simpledialog.askinteger("Withdraw", f"Your balance before withdrawal: ${balance_before}\nEnter amount:")
        if amount and amount > 0:
            success, balance_after = withdraw(username, amount)
            if success:
                messagebox.showinfo("Success", f"Withdrew ${amount}.\nBalance before withdrawal: ${balance_before}\nNew balance: ${balance_after}")
            else:
                messagebox.showerror("Failed", f"Insufficient funds.\nBalance before attempt: ${balance_before}")

    elif operation == "Transfer":
        to_user = simpledialog.askstring("Transfer", f"Your balance before transfer: ${balance_before}\nEnter recipient username:")
        amount = simpledialog.askinteger("Transfer", "Enter amount:")
        if to_user and amount and amount > 0:
            success = transfer(username, to_user, amount)
            balance_after = check_balance(username)  # Check updated balance after transfer
            if success:
                messagebox.showinfo("Success", f"Transferred ${amount} to {to_user}.\nBalance before transfer: ${balance_before}\nNew balance: ${balance_after}")
            else:
                messagebox.showerror("Failed", f"Transfer failed.\nBalance before attempt: ${balance_before}")

    elif operation == "Other Services":
        other_services_options = "Available Services:\n- Loan Application\n- Account Statement\n- Card Services\n- Customer Support\n(Features coming soon!)"
        messagebox.showinfo("Other Services", other_services_options)