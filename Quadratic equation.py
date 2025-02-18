a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=(b**2)-(4*a*c)
if d>0:
    x1=(-b+(d**0.5))/(2*a)
    x2=(-b-(d**0.5))/(2*a)
    print("The roots are real and distinct.")
    print("The roots are",x1,"and",x2)
elif d==0:
    x1=-b/(2*a)
    print("The roots are real and equal.")
    print("The root is",x1)
else:
    print("The roots are imaginary.")
    x1=-b/(2*a)
    x2=(abs(d)**0.5)/(2*a)
    print("The roots are",x1,"+ i",x2,"and",x1,"- i",x2)
    