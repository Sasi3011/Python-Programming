gsal= float(input("Enter the gross salary: "))
tax = gsal * 0.10
pf = gsal * 0.12
netsal= gsal - (tax + pf)
print("Gross Salary: ",gsal)
print("Income Tax (10%):", tax)
print("Provident Fund (12%): ",pf)
print("Net Salary:", netsal)
