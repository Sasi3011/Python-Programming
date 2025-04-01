# Replace list item with the new value if found

#
list1 = [1, 2, 3, 4, 5]
replace = 3
new = 10
if replace in list1:
    index = list1.index(replace)
    list1[index] = new
print(list1)
