#Concatenate two lists index-wise

list1 = ["M", "na", "i", "s", "h"]
list2 = ["y", "me", "s", "h", "a"]
list3 = [x + y for x, y in zip(list1, list2)]
print("Concatenated list:", list3)
