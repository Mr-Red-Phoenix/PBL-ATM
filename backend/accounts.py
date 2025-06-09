import json
import os

DATA_DIR = "C:/Users/parth sharma/Desktop/Coding/Projects/PBL_ATM/Code/data"
DATA_FILE = os.path.join(DATA_DIR, "accounts.json")

def load_accounts():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_accounts(accounts):
    with open(DATA_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def add_account(username, pin):
    accounts = load_accounts()
    if username in accounts:
        return False
    accounts[username] = {"pin": pin, "balance": 0}
    save_accounts(accounts)
    return True
