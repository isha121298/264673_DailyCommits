#Write a Python program to change the position of every n-th value with the (n+1)th in a list

l=list(input("enter the list elements").split(" "))
length=len(l)
for i in range(0,length+2):
    l[i] = l[i+1]
print("the updated list is=",l)