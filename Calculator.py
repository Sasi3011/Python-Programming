a=int(input("Enter a number: "))
b=int(input("Enter another number:"))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponent")
print("7. Floor Division")
c=int(input("Enter your choice: "))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
elif c==5:
    print(a%b)
elif c==6:
    print(a**b)
elif c==7:
    print(a//b)
else:
    print("Invalid choice")
    