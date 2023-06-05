
""" this is a simple example of aggregation (has a relation) in this type of relationship one class own
the second class, or you can say that it contains it.
Remember in aggregation the class owning the child class cannot access its private method and attributes.
"""
class Customer:

    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def changeDetails(self,new_name,new_City,new_pincode,new_state):
        self.name=new_name;
        self.address.change_address(new_City,new_pincode,new_state)


class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

    def change_address(self,new_City,new_pincode,new_state):
        self.city = new_City
        self.pincode = new_pincode
        self.state = new_state

add=Address("islamabad",700,"Capital")

cus=Customer("muzil","male",add)

print(cus.address.state)

