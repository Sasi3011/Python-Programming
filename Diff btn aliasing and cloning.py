import copy

#Difference between aliasing and cloning simple program

# Aliasing
list1 = [1, 2, 3, 4]
list2 = list1 
list2.append(5)
print("After aliasing:")
print("list1:", list1) 
print("list2:", list2)

# Cloning
list3 = [1, 2, 3, 4]
list4 = copy.deepcopy(list3) 
list4.append(5)
print("\nAfter cloning:")
print("list3:", list3)  
print("list4:", list4)