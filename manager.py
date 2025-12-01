from encryption import encrypt_data, decrypt_data
from storage import load_vault, save_vault

def add_account(fernet, name, username, password):
    vault = load_vault()
    encrypted_pw = encrypt_data(fernet, password)

    vault["accounts"].append({
        "name": name,
        "username": username,
        "password": encrypted_pw
    })

    save_vault(vault)
    print(f"[✔] Account '{name}' added.")

def view_accounts(fernet):
    vault = load_vault()
    if not vault["accounts"]:
        print("[!] No accounts stored.")
        return

    for acc in vault["accounts"]:
        decrypted_pw = decrypt_data(fernet, acc["password"])
        print(f"""
Name: {acc['name']}
Username: {acc['username']}
Password: {decrypted_pw}
-----------------------
""")

def delete_account(name):
    vault = load_vault()
    vault["accounts"] = [acc for acc in vault["accounts"] if acc["name"] != name]
    save_vault(vault)
    print(f"[✔] Account '{name}' deleted.")
