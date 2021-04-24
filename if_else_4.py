'''Write a python program to check if the input number is
-real number
-float numner
-string
-complex number
-Zero (0) '''

n=input("Enter number")
if type(int(n))==type(1):
    print("Real number")
elif type(float(n))==type(1.1):
    print("Float number")
elif n==complex():
    print("Complex Number")
elif n==0:
    print("Zero")
else:
    print("String")
