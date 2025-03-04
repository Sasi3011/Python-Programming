import cmath
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = (b**2) - (4*a*c)
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)
if d > 0:
    print("The roots are real and distinct.")
elif d == 0:
    print("The roots are real and equal.")
else:
    print("The roots are imaginary.")
print("The roots are", root1, "and", root2) 