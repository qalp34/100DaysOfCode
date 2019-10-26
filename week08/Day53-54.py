def mathsum():
    sum = 1 + 8 
    print(sum)

def mathsub():
    sub= 4 - 2
    print(sub)


def mathmult():
    mult = 6 * 6
    print(mult)
 
def mathdivi():
    divi = 8 / 2
    print(divi)


num1 = int(input(" inter Num1: "))
num2 = int(input(" inter Num2: "))
opr = input("Enter operation type (+, -, *, /):")


def math(num1, num2):
    if opr == "+" :
       res =num1 + num2
       print(res)

    elif opr == "-" :
          res = num1 - num2
          print(res)
    elif opr == "*" :
         res = num1 * num2
         print(res) 

from Day53 import*
import datetime
math(num1, num2)

print("\n-------\n")
mathsum()
mathsub()
mathmult()
mathdivi()

print("\n-------")
print("Date in python\n")

today = datetime.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print('yesterday :', yesterday)
print('today :', today)
print('tomorrow :', tomorrow)
