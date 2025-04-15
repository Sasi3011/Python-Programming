#Longest word in a file

def longest_word(file_path):
    try:
        file = open(file_path, 'r')
        words = file.read().split()
        file.close()
        longest_word = max(words, key=len)
        return longest_word
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
file_path = input("Enter the file path: ")
print("Longest word :",longest_word(file_path))