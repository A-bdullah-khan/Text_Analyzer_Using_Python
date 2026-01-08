text = input("Please enter the text: ")
letters = []

print("\n")
letters.append(input("Please enter the first letter: ").lower())
letters.append(input("Please enter the second letter: ").lower())
letters.append(input("Please enter the third letter: ").lower())
text = text.lower()

print("\n")
print("LETTER REPETITION")
letter_repetition = text.count(letters[0])
letter_repetition2 = text.count(letters[1])
letter_repetition3 = text.count(letters[2])

print("Your first letter is repeated " + str(letter_repetition) + " times")
print("Your second letter is repeated " + str(letter_repetition2) + " times")
print("Your third letter is repeated " + str(letter_repetition3) + " times")

print("\n")
print("HOW MANY LETTERS IN THE TEXT")

length = len(text)
print("Total words in your text are: " + str(length))

print("\n")
print("FIRST AND LAST LETTERS OF THE TEXT")
first_letter = text[0]
last_letter = text[-1]
print("The first letter of your text is: " + str(first_letter))
print("The last letter of your text is: " + str(last_letter))

print("\n")
print("WORDS IN INVERTED ORDER")
print("Words in inverted order : " + str(text[::-1]))

print("\n")
print("IF PYTHON IS IN THERE OR NOT")
my_bool = "python" in text
print(my_bool)

