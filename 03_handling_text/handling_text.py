print("*" * 30)
print("|       Methods to Alter Texts        |")
print("*" * 30)
print()

print("Python also provides us with methods to work with strings. Here are the most common ones:")
print("in: checks if a text is within another text.")

print()
text = "hello world how are you"
if "world" in text:
    print("the keyword is within the text")

print()
print("len: counts the number of characters in a text, including spaces")
text = "hello world how are you"
print(len(text))

print()
print("upper: converts the text to uppercase")
text = "hello world how are you"
print(text.upper())

print()
print("lower: converts the text to lowercase")
text = "HELLO WORLD"
print(text.lower())

print()
print("capitalize: converts the first letter of a string to uppercase")
text = "hello world"
print(text.capitalize())

print()
print("title: converts the first letter of each word in a string to uppercase")
text = "hello world"
print(text.title())

print()
print("count: counts the number of occurrences of a text within another text")
text = "anita washes the tub"
print(text.count("the"))

print()
print("swapcase: switches the text from uppercase to lowercase and vice versa")
text = "HeLLo WoRLd"
print(text.swapcase())

print()
print("startswith: checks if a text starts with a specific keyword")
text = "hello world"
print(text.startswith("hel"))

print()
print("endswith: checks if a text ends with a specific keyword")
text = "hello world"
print(text.endswith("ld"))

print()
print("replace: replaces one text with another within a string")
text = "hello world"
print(text.replace("world", "family"))

print()
print("isdigit: checks if a string is potentially a number")
text = "2455"
print(text.isdigit())

print()
print("strip: removes accidental spaces at the beginning and end of a string")
string = "   Hello, world!   "
trimmed_string = string.strip()
print(trimmed_string)
