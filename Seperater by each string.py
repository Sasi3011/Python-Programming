a = input("Enter a string: ")
result = ""
for i in a:
    if i == " ":
        result += "**"
    else:
        result += i
print(result)