#Second largest number in a list

def second_largest(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[1]
numbers = [10, 20, 4, 45, 99]
result = second_largest(numbers)
print("The second largest number in the list is:", result)