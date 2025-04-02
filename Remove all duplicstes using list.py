#Removes all duplicates from a list without using set()

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = remove_duplicates(input_list)
print("Original list:", input_list)
print("List after removing duplicates:", output_list)