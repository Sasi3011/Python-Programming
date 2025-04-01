#Concatneate two list in simple way

l1 = ["M", "na", "i", "s", "h"]
l2 = ["y", "me", "s", "h", "a"]
l3 = []
for i in range(len(l1)):
    l3.append(l1[i] + l2[i])
print(l3)
    