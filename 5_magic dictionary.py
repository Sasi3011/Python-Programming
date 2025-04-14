# Magic dictionary simple program without function

magic_dict = {
    "python": "A high-level programming language.",
    "algorithm": "A step-by-step procedure for solving a problem.",
    "data": "Facts and statistics collected for reference or analysis.",
    "debugging": "The process of identifying and removing errors from computer programs."
}
word = input("Enter a word to search in the magic dictionary: ").lower()
if word in magic_dict:
    print(f"{word.capitalize()}: {magic_dict[word]}")
else:
    print("Sorry, the word is not in the magic dictionary.")
