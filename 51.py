amount=int(input("Enter bill amount"))
if(amount>500):
    tc=amount+(amount*0.1)
    print("Total cost=",tc)
else:
    tc=amount
    print("Total cost=",tc)
