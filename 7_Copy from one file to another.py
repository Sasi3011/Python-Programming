#Copy from  one file to another

s = "source.txt"
d = "destination.txt"
source = open(s, "r")
content = source.read()
source.close()
destination = open(d, "w")
destination.write(content)
destination.close()