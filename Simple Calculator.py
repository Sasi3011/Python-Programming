a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
print("Enter 5 for modulus")
print("Enter 6 for exponentiation")
c=int(input("Enter your choice: "))
if c==1:
    print("Addition of the numbers is",a+b)
elif c==2:
    print("Subtraction of the numbers is",a-b)
elif c==3:
    print("Multiplication of the numbers is",a*b)
elif c==4:
    print("Division of the numbers is",a/b)
elif c==5:
    print("Modulus of the numbers is",a%b)
elif c==6:
    print("Exponentiation of the numbers is",a**b)
    