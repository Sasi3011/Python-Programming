#Remove empty strings from a list of strings

list1 = ["Hello", "", "World", "", "Python"]
list1 = [x for x in list1 if x]
print(list1)