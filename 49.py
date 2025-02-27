num = int(input("Enter a number: "))
if num == 0:
    print("The number is Zero.")
elif (num >> 31) & 1:
    print("The number is Negative.")
else:
    print("The number is Positive.")
