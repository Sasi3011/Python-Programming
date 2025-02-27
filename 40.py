n1=int(input("Enter value of a"))
n2=int(input("Enter value of b"))
n3=int(input("Enter value of c"))
mx = (n1 if (n1 > n2 and n1 > n3) else
     (n2 if (n2 > n1 and n2 > n3) else n3))
print("Max=",mx)
