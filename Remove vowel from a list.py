#remove all vowles from a list (list fuits=['apple', 'banana', 'cherry', 'date', 'fig', 'grape'])

def remove_vowels(input_list):
    vowels = 'aeiouAEIOU'
    result_list = []
    for item in input_list:
        new_item = ''.join([char for char in item if char not in vowels])
        result_list.append(new_item)
    return result_list
input_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
output_list = remove_vowels(input_list)
print("Original list:", input_list)
print("List after removing vowels:", output_list)
