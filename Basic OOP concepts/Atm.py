
"""
Encapsulation means data hiding. we make our data private and make getter and setter function to acces it. These
steps are knows as encapsulation

remember in python nothing is really private we don't have any private or protected keywords to make our data private we
use __ with varibales name to show that they are private.

what the __ does is that it creates the variable in memory as _Atm__pin so that we try to access like this
a =Atm()
a.__pin then it will not really access the real data. but i we use this syntax a._Atm.__pin then we can access the
attribute pin
"""
class Atm:
    def __init__(self):
        self.__pin=""
        self.balance=0

        self.menu

    def menu(self):
        user_input=input(""" 
        Hello how would you likr to proceed 
        1. Enter 1 to create __pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to Exit
        """)
        if user_input=="1":
            self.create___pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            exit()

    def create___pin(self):
        self.____pin=input("Enter your __pin")
        print("print updated successfully")
    def deposit(self):
        temp=input("Enter your __pin")
        if temp==self.__pin:
            amount=int(input("enter the amount"))
            self.balance=self.balance + amount
            print("deposited successfully")
        else:
            print("You Entered Wrong __pin")
    def withdraw(self):
        temp = input("Enter your __pin")
        if temp==self.__pin:
            amount=int(input("enter the amount you want to withdraw"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation successfull")
            else:
                print("Insufficient Funds")
        else:
            print("You entered Wrong __pin")
    def check_balance(self):
        temp = input("Enter your __pin")
        if temp==self.__pin:
            print(self.balance)
        else:
            print("you entered Wrong __pin")

    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        self.__pin=new_pin