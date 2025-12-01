from encryption import get_master_key
from manager import add_account, view_accounts, delete_account
from password_generator import generate_password
from rich.console import Console
from config import admin_password

console = Console()

def menu():
    console.print("""
[cyan]
1. Add account
2. View accounts
3. Delete account
4. Generate password
5. Exit
[/cyan]
""")

def admin_only():
    while True:
        getpassword = input("Enter Admin Password: ")
        if getpassword == admin_password:
            console.print("[green] [✅] Successfully Logged In")
            break
        else:
            console.print("[red] [x] Invalid Admin Password")

def main():
    fernet = get_master_key()
    admin_only()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Account name: ")
            username = input("Username: ")
            password = input("Password (leave blank to auto-generate): ")

            if not password:
                password = generate_password()
                print(f"[Generated password]: {password}")

            add_account(fernet, name, username, password)

        elif choice == "2":
            view_accounts(fernet)

        elif choice == "3":
            name = input("Enter account name to delete: ")
            delete_account(name)

        elif choice == "4":
            length = int(input("Length of password: "))
            print("Generated:", generate_password(length))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
