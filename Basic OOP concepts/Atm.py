class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0

        self.menu

    def menu(self):
        user_input=input(""" 
        Hello how would you likr to proceed 
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to Exit
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            exit()

    def create_pin(self):
        self.pin=input("Enter your pin")
        print("print updated successfully")
    def deposit(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount"))
            self.balance=self.balance + amount
            print("deposited successfully")
        else:
            print("You Entered Wrong pin")
    def withdraw(self):
        temp = input("Enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount you want to withdraw"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation successfull")
            else:
                print("Insufficient Funds")
        else:
            print("You entered Wrong pin")
    def check_balance(self):
        temp = input("Enter your pin")
        if temp==self.pin:
            print(self.balance)
        else:
            print("you entered Wrong pin")

