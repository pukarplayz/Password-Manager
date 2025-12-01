import json
from config import VAULT_FILE

def load_vault():
    try:
        with open(VAULT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"accounts": []}

def save_vault(data):
    with open(VAULT_FILE, "w") as f:
        json.dump(data, f, indent=4)
