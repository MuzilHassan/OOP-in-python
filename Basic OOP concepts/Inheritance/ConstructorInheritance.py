class phone:

    def __init__(self,price ,brand ,camera):

        self.price=price
        self.brand=brand
        self.camera=camera


class smartPhone(phone):
    pass


smrtphone= smartPhone(89,"samsung","48px")


print(smrtphone.price)
