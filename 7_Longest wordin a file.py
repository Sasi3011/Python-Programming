def longest_word(file_path):
    try:
        with open(file_path) as file:
            return max(file.read().split(), key=len)
    except Exception as e:
        return f"Error: {e}"
print("Longest word:", longest_word(input("Enter the file path: ")))
