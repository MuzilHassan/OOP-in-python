"""this is simple demo to show how inheritance is done in python
   Inheritance means is a realtion . here child class have all the properties of its parent like
   its constructor its method and attributes.
   But the same is not true for parent
"""

class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


class Student(User):
    def enroll(self):
        print("enroll")

    def drop(self):
        print("drop")

student= Student()

student.login()
student.enroll()