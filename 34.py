number = int(input("Enter a number: "))
if number & 1 == 0:
    result = "Even"
else:
    result = "Odd"
print(f"The number {number} is {result}.")