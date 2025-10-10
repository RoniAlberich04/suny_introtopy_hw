sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")

if letter in sentence:
    count = sentence.count(letter)
    print(f"Letter '{letter}' appears {count} time(s).")
else:
    print(f"Letter '{letter}' does not appear.")