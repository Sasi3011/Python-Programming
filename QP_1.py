# Ex.1 Create a Python application that uses expressions and control flow statements to automate a common task. Ensure that your application is user-friendly and robust to different inputs
#     a. Swap two numbers without a temporary variable, 
#     b. Quadratic Equation, 
#     c.Valid Palindrome  

# a. Swap two numbers without a temporary variable

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Before swapping :", a, b)
a=a+b
b=a-b
a=a-b
print("After swapping :", a, b)

# b. Quadratic Equation

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=(b**2)-(4*a*c)
sol1=(-b+d**0.5)/(2*a)
sol2=(-b-d**0.5)/(2*a)
print(f"The solutions are %.2f and %.2f" %(sol1, sol2))

# c. Valid Palindrome

a=input("Enter a string: ")
a=a.lower()
b=a[::-1]
if a==b:
    print("It is a palindrome")
else:
    print("It is not a palindrome")