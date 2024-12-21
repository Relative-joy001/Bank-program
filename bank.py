# banking program functions

recipient_details = dict()

def show_balance(balance):
    print("*********************")
    print(f"Your current balance is: ${balance:,.2f}")
    print("*********************")

def add_recipient():
    print("*********************")
    name = input("Enter the recipient's Full name: ")
    print("*********************")
    account_number = int(input("Enter the recipient's account number: "))
    print("*********************")
    recipient_details[account_number] = (name)
    print(f"Recipient '{name}' added successfully.")

def view_all_recipients():
    print("*********************")
    print("All Recipients:")
    print("*********************")
    for account_number, name in recipient_details.items():
        print(f"Account Number: {account_number}, Name: {name}")

def deposit():
    print("*********************")
    amount = float(input("Enter the amount to deposit: "))

    if amount < 0:
        print(f"This is not a valid deposit amount. Please try again.")
        return 0
    else:
        print("Deposit Completed Successfully.")
        print("*********************")
        return amount
    
    
def withdraw(balance):
    print("*********************")
    amount = float(input("Enter the amount to withdraw: "))
    

    if amount > balance:
        print(f"Insufficient funds.")
    elif amount < 0:
        print("Amount must be a greater than zero.")
        return 0
    else:
        print("Withdrawal Completed Successfully.")
        print("*********************")
        return amount
    
def transfer(balance):
    add_recipient()
    amount = float(input("Enter the amount to transfer: "))

    if amount > balance:
        print(f"Insufficient funds.")
        return 0
    elif amount < 0:
        print("Amount must be a greater than zero.")
        return 0
    else:
        print("Transfer Completed Successfully.")
        print("*********************")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("    Banking Program   ")
        print("*********************")

        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Add Recipient")
        print("6. View Recipients List")
        print("7. Exit")
        print("*********************")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            balance -=transfer(balance)
        elif choice == 5:
            add_recipient()
        elif choice == 6:
            view_all_recipients()
        elif choice == 7:
            is_running = False
        else:
            print("*********************")
            print("Invalid choice. Please try again.")
    print("*********************")
    print("Thank you for using our banking program!")
    print("*********************")


if __name__ == "__main__":
    main()