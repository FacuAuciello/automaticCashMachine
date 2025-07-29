#AUTOMATIC CASH MACHINE

#MENU
def main_menu():
    print("WELCOME TO THE AUTOMATIC CASH MACHINE TESLA 2.0\n1)Create account\n2)Enter account\n3)Exit")
    user_option = int(input("Select an option: "))
    return user_option
#CREATE ACCOUNT
def create_account():
    pass

def full_name():
    pass
def ID():
    pass
def pin_password():
    pass
#una vez que llega aca vuelve al menu para ingresar a su cuenta
#ENTER ACCOUNT
def enter_account():
    pass
#se podria utilizar la misma funcion para entrar a la cuenta, con la funcion dni y password?
def account_menu():
    pass
def see_balance():
    pass
def deposit():
    pass
def withdraw(): #retirar
    pass
def exit ():
    pass #tambien podria utilizar la de exit del programa?
#EXIT
def exit():
    pass

continuar = True
while continuar:
    main_menu()
    #if user_option == 1:

class bankAccount:
    def __init__(self, name, lastName, ID, pinPassword):
        self.name = name
        self.lastName = lastName
        self.ID = ID
        self.pinPassword = pinPassword
    
    def name(self):
        user_name = input("Enter your name: ")
        return user_name
    
    def lastName(self):
        user_last_name = input("Enter your last name: ")
        return user_last_name

    def ID(self):
        user_ID = int(input("Enter your ID: "))
        if user_ID == len(8):
            return ID
        else:
            print("Enter only eigth numbers")
    
    def pinPassword():
        user_pin_password = int(input("Enter your pin password(four numbers): "))
        if user_pin_password == len(4):
            return user_pin_password
        else:
            print("Enter only four numbers")
