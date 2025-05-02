class supermarkert:
    pname=input("Enter the product name: ")
    qty=int(input("Enter the quantity: "))
    price=int(input("Enter the price: "))
s=supermarkert()
print("Product name:",s.pname)
print("Quantity:",s.qty)
print("Price:",s.price)
print("Total price:",s.qty*s.price)