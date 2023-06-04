from Atm import Atm
from Fraction import Fraction
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num=Fraction(5,8)
    num2=Fraction(6,7)

    print(num*num2)
    print(num/num2)

    print(num)

    a= Atm()
    a.menu()
    a.deposit()
    a.check_balance()
    a.withdraw()
    a.check_balance()