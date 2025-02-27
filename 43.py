num=int(input("Enter a number"))
s=0
while(num!=0):
    rem=num%10
    s+=rem
    num=num//10
print("Sum=",s)
