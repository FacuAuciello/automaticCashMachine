#AUTOMATIC CASH MACHINE

#CLASS Y FUNCTIONS
class BankAccount:
    def __init__(self, name, lastName, ID, pinPassword, balance=0):
        self.name = name
        self.lastName = lastName
        self.ID = ID
        self.pinPassword = pinPassword
        self.balance = balance

    def see_balance(self):
        print(f"Your balance is: ${self.balance}")

    def deposit(self):
        user_deposit = input("Enter the amount to deposit: ")
        if user_deposit.isdigit():
            user_deposit = int(user_deposit)
            self.balance += user_deposit
            print(f"Deposit successful. Your new balance is: ${self.balance}")
        else:
            print("Invalid input. Deposit must be a number.")

    def withdraw(self):
        user_withdraw = input("Enter the amount to withdraw: ")
        if user_withdraw.isdigit():
            user_withdraw = int(user_withdraw)
            if user_withdraw <= self.balance:
                self.balance -= user_withdraw
                print(f"You withdrew ${user_withdraw}. Your new balance is: ${self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid input. Withdrawal must be a number")


def main_menu():
    print("#### WELCOME TO THE AUTOMATIC CASH MACHINE TESLA 2.0 ####\n1)Create account\n2)Enter account\n3)Exit")
    user_option_main_menu = input("----------Select an option----------:")
    if user_option_main_menu.isdigit() and len(str(user_option_main_menu)) == 1:
        user_option_main_menu = int(user_option_main_menu)
    else:
        print("INVALID. Enter a correct option ")
        user_option_main_menu = 0
    return user_option_main_menu


def create_account():
    user_name = input("Enter your name: ")
    user_last_name = input("Enter your last name: ")
    user_ID = int(input("Enter your ID. Only eight numbers: "))
    user_pin_password = int(input("Enter your pin password(four numbers): "))
    new_account = BankAccount(user_name, user_last_name, user_ID, user_pin_password)
    accounts.append(new_account)
    print("----Account created successfully----\n----Now you can log in to your account----")


def enter_account(accounts):
    while True:
        user_ID = input("Enter your ID. Only eight numbers: ")
        if user_ID.isdigit() and len(str(user_ID)) == 8:
            user_ID = int(user_ID)
            break
        else:
            print("INVALID. Please enter your eight numbers ID correctly ")

    while True:
        user_pin_password = input("Enter your pin password(four numbers): ")
        if user_pin_password.isdigit() and len(str(user_pin_password)) == 4:
            user_pin_password = int(user_pin_password)
            break
        else:
            print("INVALID. Please enter your pin password correctly ")

    for account in accounts:
        if account.ID == user_ID and account.pinPassword == user_pin_password:
            return account

    print("Incorrect ID or PIN. Please try again.")
    return None


def account_menu():
    print("----What do you want to do?----\n1)See balance\n2)Deposit\n3)Withdraw\n4)Return to menu")
    user_option_account_menu = input("Select an option: ")
    if user_option_account_menu.isdigit() and len(str(user_option_account_menu)) == 1:
        user_option_account_menu = int(user_option_account_menu)
    else:
        print("INVALID. Enter a correct option ")
        user_option_account_menu = 0
    return user_option_account_menu


def exit_program():
    print("Bye")

#LOGIC
accounts = []

while True:
    option_user = main_menu()
    if option_user == 1:
        create_account()
    elif option_user == 2:
        while True:
            logged_account = enter_account(accounts)
            if logged_account is not None:
                while True:
                    option_menu_account = account_menu()
                    if option_menu_account == 1:
                        logged_account.see_balance()
                    elif option_menu_account == 2:
                        logged_account.deposit()
                    elif option_menu_account == 3:
                        logged_account.withdraw()
                    elif option_menu_account == 4:
                        break
                    else:
                        print("Invalid option")
                break
    elif option_user == 3:
        exit_program()
        break
    else:
        print("Invalid. Enter a valid option")