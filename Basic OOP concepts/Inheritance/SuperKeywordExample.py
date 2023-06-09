
"""Super keyword is used to access parent methods and constructor.
   Remember one thing that we cannot super outside class
   Super keyword should be first line whrn used inside constructor
   """

class phone:

    def __init__(self,price ,brand ,camera):

        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Selling phone")
class smartPhone(phone):

    def __init__(self,price ,brand ,camera,os,ram):
        super().__init__(price ,brand ,camera)
        self.os=os
        self.ram=ram
        


    def buy(self):
        print("selling smart phone")

        super().buy()


smrtphone= smartPhone(89,"samsung","48px","android","4gb")


print(smrtphone.buy())
print(smrtphone.os)