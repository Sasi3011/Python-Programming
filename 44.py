num = int(input("Enter a number: "))

if num > 0 and (num & (num - 1)) == 0:
    print(num,"is a power of 2.")
else:
    print(num,"is NOT a power of 2.")
