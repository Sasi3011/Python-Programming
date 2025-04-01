#Remove all occurrences of a specific value from a list

list= [1, 2, 3, 4, 5, 3, 6]
remove = 3
while remove in list:
    list.remove(remove)
print(list)
