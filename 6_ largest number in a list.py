# largest number in a list

def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
numbers = [10, 20, 4, 45, 99]
print("The largest number is:", find_largest_number(numbers))