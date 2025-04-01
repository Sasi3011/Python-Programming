#Method 1: Using the reverse() method
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print("Reversed list using reverse():", list1)

#Method 2: Using slicing
list2 = [1, 2, 3, 4, 5]
list2 = list2[::-1]
print("Reversed list using slicing:", list2)

#Method 3: Using the reversed() function
list3 = [1, 2, 3, 4, 5]
list3 = list(reversed(list3))
print("Reversed list using reversed():", list3)

#Method 4: Using a loop
list4 = [1, 2, 3, 4, 5]
reversed_list = []
for item in list4:
    reversed_list.insert(0, item)
print("Reversed list using a loop:", reversed_list)

