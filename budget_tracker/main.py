import csv


def login():
    accounts = {
            "brandon": "Simpson",
            "emma": "Alright123",
            "admin": "password"
        }
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if username in accounts and accounts[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password. Try again.")


def add_transaction(username):
    try:
        open(f"{username}_budget.csv", "r").close()
        file_exists = True
    except FileNotFoundError:
        file_exists = False

    transaction = {}
    transaction["type"] = input("Enter transaction type (income/expense): ")
    transaction["amount"] = float(input("Enter transaction amount: $ "))
    transaction["description"] = input("Enter transaction description: ")

    with open(f"{username}_budget.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["type", "amount", "description"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(transaction)
    
    print("Transaction added successfully!\n")


def start_menu():
    print("Welcome to the Budget Tracker!")
    print("1. Log in")
    print("2. Exit program")

def account_menu(username):
    print(f"\nWelcome, {username}!")
    print("1. Add transaction")
    print("2. Log out")

def main():
    while True:
        start_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            username = login()
            if username:
                while True:
                    account_menu(username)
                    account_choice = input("Enter your choice: ")
                    if account_choice == "1":
                        add_transaction(username)
                    elif account_choice == "2":
                        print("Logging out...\n")
                        break
        elif choice == "2":
            print("Exiting program...")
            return True
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()