![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Security](https://img.shields.io/badge/encryption-Fernet%20AES-orange)
![Status](https://img.shields.io/badge/status-active-brightgreen)


# 🔐 Password Manager  
A clean, secure, and lightweight **local password manager** built with Python.  
Designed for developers who want **full control** over their data without relying on cloud storage.

This tool encrypts all saved passwords using **PBKDF2-HMAC (SHA-256)** + **Fernet AES encryption**, ensuring your credentials remain safe even if the vault file is accessed.

---

## ✨ Features

### 🔑 Strong Encryption  
- Master password used to derive a cryptographic key  
- PBKDF2 with 390,000 iterations  
- Unique salt for extra protection  
- Fernet (AES-128 + HMAC) encryption

### 🧱 Two-Layer Authentication  
- **Master Password** → Unlock encryption  
- **Admin Password** → Access dashboard

### 📦 Account Vault System  
- Add new accounts  
- View decrypted credentials  
- Delete accounts  
- All accounts stored securely in `vault.json`

### 🔧 Utility Tools  
- Built-in **strong password generator**  
- Clean modular codebase  
- Designed for easy extension

---

## 🗂 Project Structure

```
📁 password-manager/
│── main.py
│── encryption.py
│── manager.py
│── storage.py
│── password_generator.py
│── config.py
│── vault.json             # Auto-generated (encrypted)
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/pukarplayz/Password-Manager.git
cd password-manager
```

### 2. Install required packages
```bash
pip install cryptography rich
```

---

## 🔧 Configuration

Adjust your credentials in `config.py`:

```python
SALT = b"yoursecretsalt"
master_key = "your_password"
VAULT_FILE = "vault.json"
admin_password = "your_admin_password"
```

⚠️ **Important:** Always replace these with your own secure values before actual use.

---

## ▶️ Running the App

Start the tool:

```bash
python main.py
```

### Login Flow  
1. Enter **master password** → generates encryption key  
2. Enter **admin password** → unlocks menu  

---

## 🖥 Menu Options

```
1. Add account
2. View accounts
3. Delete account
4. Generate password
5. Exit
```

Simple, clean, and easy to use.

---

## 🔐 Example Usage

### Adding an Account
```
Account name: GitHub
Username: test123
Password (leave blank to auto-generate):

[✔] Account 'GitHub' added.
```

### Viewing Accounts
```
Name: GitHub
Username: test123
Password: d8G@f#2sW!p1
-----------------------
```

---

## 🛡 Security Breakdown

Your data is always protected using:

- **PBKDF2HMAC (SHA-256)** → Derives key from master password  
- **390k iterations** → Extremely resistant to brute force  
- **Salted keys** → Prevent rainbow table attacks  
- **AES-128 w/ HMAC authentication** → Ensures confidentiality + integrity  

Even if someone gets your `vault.json`, they **cannot decrypt it** without the correct master password.

---

## 🧩 Customization Ideas

Want to expand the project? Here are some ideas:

- 🔎 Search accounts  
- 🏷 Category folders  
- 🔄 Export/Import encrypted vault  
- 🌐 Web dashboard (Flask/FastAPI)  
- 🖥 GUI (Tkinter/PyQt6)  
- 📌 Clipboard auto-clear  

If you want me to build any of these for you, just say the word.

---

## 📜 License

This project is **MIT Licensed**.  
Feel free to modify, extend, and use it however you like.

---

## 🤝 Contributing

PRs and feature suggestions are always welcome.  
Let’s build something awesome together.

---

## ⭐ Support

If you like the project, consider giving it a **star** on GitHub — it helps a lot!

