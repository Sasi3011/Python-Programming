#wordcount in a file

# filename = "sample.txt"
# try:
#     file = open(filename, "r")
#     words = file.read().split()
#     file.close()
#     print(f"Word count: {len(words)}")
# except FileNotFoundError:
#     print(f"The file {filename} does not exist.")


# wordcount

f = open("sample.txt", "r")
data = f.read()
words = data.split()
word_count = len(words)
print(word_count)