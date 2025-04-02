#function that returns a list containing only the squares of the given numbers

def squares(numbers):
    return [number ** 2 for number in numbers]
numbers = [1, 2, 3, 4, 5]
result = squares(numbers)
print("Squares of the given numbers:", result)