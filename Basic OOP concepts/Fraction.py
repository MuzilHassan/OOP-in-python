class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.dnum=d

    def __str__(self):
        return "{}/{}".format(self.num,self.dnum)

    def __add__(self, other):
        temp=self.num*other.dnum + self.dnum*other.num
        return "{}/{}".format(temp, self.dnum*other.dnum)

    def __sub__(self, other):
        temp = self.num * other.dnum - self.dnum * other.num
        return "{}/{}".format(temp, self.dnum * other.dnum)
    def __mul__(self, other):
        return "{}/{}".format(self.num * other.num, self.dnum * other.dnum)

    def __truediv__(self, other):
        temp = self.num * other.dnum
        temp2=self.dnum * other.num
        return "{}/{}".format(temp,temp2)