# 'r' mode
file = open("Sample.txt", "r")  # Open the file in 'r' mode
content = file.read()
print(content)
file.close()

# 'w' mode
file = open("Sample.txt", "w")
file.write("This is written using 'w' mode.\n")
file.close()

# 'a' mode
file = open("Sample.txt", "a")
file.write("This is appended using 'a' mode.\n")
file.close()

# 'r+' mode
file = open("Sample.txt", "r+")
file.write("This is written using 'r+' mode.\n")  
content = file.read()
print(content)
file.close()

# 'w+' mode
file = open("Sample.txt", "w+")
file.write("This is written using 'w+' mode.\n")
content = file.read()
print(content)
file.close()

# 'a+' mode
file = open("Sample.txt", "a+")
file.write("This is appended using 'a+' mode.\n")  
content = file.read()
print(content)
file.close()
