#Add new item to list after a specific item

list1 = [1, 2, 3, 4, 5]
item_to_add = 6
specific_item = 3
index = list1.index(specific_item) + 1
list1.insert(index, item_to_add)
print(list1)
