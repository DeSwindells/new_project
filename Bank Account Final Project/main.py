# main.py RoboGarden Bank Account Final Project
# Demian Swindells 2/28/2024
# Create a class for the bank account operation;
# Implement multiple functions that are each specialized in only one account operation; 
# And Test your bank account class by applying multiple operations.
from random import randint
class BankAccount:
 
    # Constructor
    def __init__(self, name, accountType, balance = 0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = randint(1000, 2000)
        self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        f = open(self.filename, 'a')
        f.close()

    #  Function to create and add a new Bank Account
    def add_account(self, name, accountType, balance):
        accnt = BankAccount(name, accountType, balance)
        f = open(accnt.filename, 'a')
        f.writelines("Opening Balance: $" + str(accnt.balance) + '\n')
        f.close()
        print("Account has been Created:")
        accnt.display_info(accnt)
        lst.append(accnt)

    # Function to display Account Details
    def display_info(self, accnt):
        print("Name : ", accnt.name)
        if accnt.accountType == 1:
            print("Account Type : Checkings")
        elif accnt.accountType == 2:
            print("Account Type : Savingss")
        print("Balance : $", accnt.balance)
        print("Account Number: ", accnt.accountNumber)
        print("Account File: ", accnt.filename)
        print("\n")

    # Function to make a Deposit to an Account
    def accnt_Deposit(self, accnt, balance):
        f = open(accnt.filename, 'a')
        f.write("\nBalance Statement: $" + str(accnt.balance) + '\n')
        accnt.balance += balance
        f.write("Deposited: $" + str(balance) + '\n')
        f.write("New Balance: $" + str(accnt.balance) + '\n')
        f.close()
        print("Deposit has been confirmed\n")

    # Function to make a Withdrawl from an Account
    def accnt_Withdraw(self, accnt, balance):
        f = open(accnt.filename, 'a')
        f.write("\nBalance Statement: $" + str(accnt.balance) + '\n')
        accnt.balance -= balance
        f.write("Withdrawn: $" + str(balance) + '\n')
        f.write("New Balance: $" + str(accnt.balance) + '\n')
        f.close()
        print("Withdrawl has been confirmed\n")

    # Function to read an account statement
    def accnt_Statement(self, accnt):
        f = open(accnt.filename, 'r')
        lines = f.readlines()
        for x in range(len(lines)):
            print(lines[x])

def create_ui_lst():
    ui_lst.append("Plese enter a number from the list of options below:")
    ui_lst.append(". Create Account")
    ui_lst.append(". View List of Accounts")
    ui_lst.append(". View Account Info")
    ui_lst.append(". View Account Statement")
    ui_lst.append(". Make Deposit to Account")
    ui_lst.append(". Make Withdrawl from Account")
    ui_lst.append(". Stop The Program")
    return

def display_ui_lst():
    for i in range(len(ui_lst)):
        if i == 0:
            print(ui_lst[i])
        else:
            print(i, ui_lst[i])


# Create Public lists
lst = []
ui_lst = []

# create objet of the Books Class
obj = BankAccount("", "", 0)
create_ui_lst()

run = True
while run:
    display_ui_lst()
    try:
        user_input = int(input("Your choice: "))
    except:
        print("Please try again. Input must be a Number\n")
        continue
    if user_input <= 0 or user_input >= 8:
        print("Please Try again. Input must be from the list provided.\n")
        continue

    # checks if user input is 1: Create Account
    if user_input == 1:
        selected = False
        print("Create Account:")
        name = input("Enter Your Name: ")
        while not selected :
            accnt_choice = int(input("Choose Account type:\n1. Checkings\n2. Savings\n"))
            if accnt_choice <=0 or accnt_choice >= 3:
                print("Please Try again. Input must be from the list provided.\n")
                continue
            else:
                selected = True
                if accnt_choice == 1:
                    accountType = 'Checkings'
                else:
                    accountType = 'Savings'
                break
        balance = int(input("Enter Oppening Balance: "))
        obj.add_account(name, accountType, balance)
        #obj.display_info(accnt)
        continue
    # checks if user input is 2: View Accounts
    elif user_input == 2:
        print("List of Accounts:\n")
        for i in range(lst.__len__()):
            obj.display_info(lst[i])
        continue
    # checks if user input is 3: View Account info
    elif user_input == 3:
        crrct = False
        while not crrct:
            accnt = int(input("Please Enter Account Number to view info: "))
            for i in range(lst.__len__()):
                if accnt == lst[i].accountNumber:
                    obj.display_info(lst[i])
                    crrct = True
                    break
                else:
                    print("That Account Number does not exist. Please try again.")
                    continue
        continue
    # checks if user input is 4: View Account Statements
    elif user_input == 4:
        crrct = False
        while not crrct:
            accnt = int(input("Please Enter Account Number to view statement: "))
            for i in range(lst.__len__()):
                if accnt == lst[i].accountNumber:
                    obj.accnt_Statement(lst[i])
                    crrct = True
                    break
                else:
                    print("That Account Number does not exist. Please try again.")
                    continue
        continue
    # checks if user input is 5: Make Deposit
    elif user_input == 5:
        if lst.__len__() <= 0:
            print("No Accounts Currently Open. Please Open An Account.")
            continue
        else:
            accnt_exist = False
            crrct = False
            while not accnt_exist:
                accnt = int(input("Please Enter Account Number to make Withdrawl: "))
                for i in range(lst.__len__()):
                    if accnt == lst[i].accountNumber:
                        accnt_exist = True
                        while not crrct:
                            try:
                                amnt = int(input("Please Enter the amount you would like to Deposit: "))
                                crrct = True
                            except:
                                print("Please try again. Input must be a Number\n")
                                continue
                        for i in range(lst.__len__()):
                            if name == lst[i].name:
                                obj.accnt_Deposit(lst[i], amnt)
                    else:
                        print("That Account Number does not exist. Please try again.")
                        continue
    # checks if user input is 6: make withdrawl
    elif user_input == 6:
        if lst.__len__() <= 0:
            print("No Accounts Currently Open. Please Open An Account.")
            continue
        else:
            accnt_exist = False
            over_limit = True
            crrct = False
            while not accnt_exist:
                accnt = int(input("Please Enter Account Number to make Withdrawl: "))
                for i in range(lst.__len__()):
                    if accnt == lst[i].accountNumber:
                        accnt_exist = True
                        while over_limit:
                            while not crrct:
                                try:
                                    amnt = int(input("Please Enter the amount you would like to Withdraw: "))
                                    crrct = True
                                except:
                                    print("Please try again. Input must be a Number\n")
                                    continue
                            for i in range(lst.__len__()):
                                if name == lst[i].name:
                                    if amnt > lst[i].balance:
                                        print("Withdrawl amount is greater than Account Balance. Please try again")
                                        crrct = False
                                        break
                                    elif amnt <= lst[i].balance:
                                        obj.accnt_Withdraw(lst[i], amnt)
                                        over_limit = False
                                        break
                                break
                    else:
                        print("That Account Number does not exist. Please try again.")
                        continue           
    # checks if the user input is 7: terminate program
    elif user_input == 7:
        print("Thankyou, Program has been stopped.")
        run = False
        break
    else:
        print("Please choose from the list provided")
        continue