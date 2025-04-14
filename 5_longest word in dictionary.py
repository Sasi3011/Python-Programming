#longest word in dictionary
# Create a dictionary with some words

words = ["apple", "banana", "cherry", "date", "elderberry"]

# Find the longest word
longest_word = max(words, key=len)

print("The longest word in the dictionary is:", longest_word)