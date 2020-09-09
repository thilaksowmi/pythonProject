# Simple Calculator

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a // b


print(""" Select Operation
1.add
2.sub
3.mul
4.div
""")
choice = int(input("Enter your Choice"))
a = int(input("Enter Number1= "))
b = int(input("Enter Number2= "))
if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(sub(a, b))
elif choice == 3:
    print(mul(a, b))
elif choice == 4:
    print(div(a, b))
else:
    print("Enter Correct Choice")
