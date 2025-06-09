from .accounts import load_accounts, save_accounts
from datetime import datetime
import os

TRANSACTION_LOG = "C:/Users/parth sharma/Desktop/Coding/Projects/PBL_ATM/Code/data/transactions.txt"

def log_transaction(entry):
    os.makedirs("C:/Users/parth sharma/Desktop/Coding/Projects/PBL_ATM/Code/data", exist_ok=True)
    with open(TRANSACTION_LOG, "a") as f:
        f.write(f"{datetime.now()} - {entry}\n")

def check_balance(username):
    accounts = load_accounts()
    return accounts[username]['balance']

def deposit(username, amount):
    accounts = load_accounts()
    accounts[username]['balance'] += amount
    save_accounts(accounts)
    log_transaction(f"{username} deposited {amount}")
    return accounts[username]['balance']

def withdraw(username, amount):
    accounts = load_accounts()
    if accounts[username]['balance'] >= amount:
        accounts[username]['balance'] -= amount
        save_accounts(accounts)
        log_transaction(f"{username} withdrew {amount}")
        return True, accounts[username]['balance']
    return False, accounts[username]['balance']

def transfer(sender, receiver, amount):
    accounts = load_accounts()
    if receiver not in accounts or accounts[sender]['balance'] < amount:
        return False
    accounts[sender]['balance'] -= amount
    accounts[receiver]['balance'] += amount
    save_accounts(accounts)
    log_transaction(f"{sender} transferred {amount} to {receiver}")
    return True
