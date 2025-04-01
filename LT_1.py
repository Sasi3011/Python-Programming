#Second largest number in a list in simple

def second_largest(numbers):
    first = second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second
numbers = [10, 20, 4, 45, 99]
print("The second largest number is:", second_largest(numbers))
