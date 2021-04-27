# Write a Python program to convert a list into a nested dictionary of keys

list1 = list(input("enter the list elements").split(" "))
dict1 = current1 = {}
for name in list1:
    current1[name] = {}
    current1 = current1[name]
print(dict1)