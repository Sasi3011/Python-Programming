#example 1
a=[1,2,3,4,5]
b=a[:]
print(b)
#example 2
a=[1,2,3,4,5]
b=a[:]
a[0]=0
print("a:",a)
print("b:",b)
#example 3
a=[1,2,3,4,5]
b=a[:]
b[0]=0
print("a:",a)
print("b:",b)
#example 4
a=[1,2,3,4,5]
b=a[:]
a[0]=0
b[1]=0
print("a:",a)
print("b:",b)