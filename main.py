import string

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    print(len(words))

    letters = dict.fromkeys(string.ascii_lowercase, 0)
    print(letters)
    num_words = len(words)
    count = 0

    for word in words:
        count += 1
        print("processing " + str(count) + " out of " + str(num_words))
        for i in word:
            letter = i.lower()
            if letter in letters:
                letters[letter] += 1

    print("--- Begin report of books/frankenstein.txt ---\n")
    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---\n")