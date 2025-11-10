phrase = "Python Programming"
print(phrase[0:6])
print(phrase[7:])
print(phrase[:6])
print(phrase[::2])
print(phrase[::-1])

text = "the Quick Brown Fox"
print(text.lower())
print(text.upper())
print(text.title())

print(text.capitalize())
print(text.swapcase())

example = "Hello, World! 123"
# Searching
print(example.find("World"))
 # 7
print(example.find("Universe"))  # -1
print(example.index("World"))    # 7 (raises an error if not found)
print(example.rfind("l"))
print(example.count("l"))
 # 10
   # 3

mess = "   Some text with extra spaces   "
example2 = "...Hello, World!..."
print(mess.strip())
print(mess.lstrip())
print(mess.rstrip())
print(example2.strip("."))
# Removes surrounding whitespace
# Removes from left only
# Removes from right only
 # Removes dots from both ends
original = "She loves cats. Her cat is lovely."
print(original.replace("cat", "dog"))
  # Replaces all
print(original.replace("cat", "dog", 1))    # Replaces only the first
tabbed = "one\ttwo\tthree"
print(tabbed.expandtabs(4))

