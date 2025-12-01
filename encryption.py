import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from config import SALT, master_key
from rich.console import Console

console = Console()

def get_master_key():
    while True:
        master_password = input("Enter master password: ")

        if master_password != master_key:
            console.print("[red] [x] Invalid Master Key")
            continue
        else:
            console.print("[green] [✅] Accepted Master Key")
            break

    master_bytes = master_password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=390000,
        length=32,
        salt=SALT
    )

    key = base64.urlsafe_b64encode(kdf.derive(master_bytes))
    return Fernet(key)


def encrypt_data(fernet, data: str):
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(fernet, token: str):
    return fernet.decrypt(token.encode()).decode()
