# Ask the user to enter a word
word = input("Enter a word: ")

#Display the word in different formats
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())
print("Capitalised:",word.capitalize())
print("Title Case:", word.title())
print("Swap Case:", word.swapcase())

# Reverse the word using slicing
print("Reversed:", word[::-1])

# Count the number of characters
print("Number of characters:", len(word))

#Check membership of the letter 'a'
print("Does the word contain 'a'? :", 'a' in word)  # Return as True / False


text = " Hello, Python World! "

# Trim spaces
print("Original:", repr(text))
print("Strip both sides:", repr(text.strip))
print("Strip left:", repr(text.lstrip()))
print("Strip right:", repr(text.rstrip()))

# Replace characters
new_text = text.replace("Python", "Programming")
print("After replace:", repr(new_text))
new_text2 = text.replace(" ", "_")
print("Spaces replaced with underscores:", repr(new_text2))

# Align text
print("Centre aligned:", text.strip().center(30, "-"))
print("Left aligned:", text.strip().ljust(30, "."))
print("Right aligned:", text.strip().rjust(30, "."))

#Count letters
letter_count = text.count("p")
print("Number of 'p' in text:", letter_count)

#Test for prefixes/suffixes
print("Start with 'Hello':", text.strip().startswith("Hello"))
print("End with 'World':", text.strip().endswith("World!"))

processed = text.strip().replace("Python", "Programming").upper()
print("Processed text:", processed)
print("Does text start with 'HELLO'? :", processed.startswith("HELLO"))

