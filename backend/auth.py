from .accounts import load_accounts

def authenticate(username, pin):
    accounts = load_accounts()
    return username in accounts and accounts[username]['pin'] == pin
