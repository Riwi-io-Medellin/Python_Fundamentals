print("*" * 30)
print("|         TUPLES IN PYTHON         |")
print("*" * 30)
print()

# What is a tuple?
print("1. What is a tuple?")
print("Tuples are similar to lists, but they are immutable, meaning they cannot be changed after creation.")
print("They are defined using parentheses () instead of square brackets [].")
print()

# Creating a tuple
print("2. Creating tuples")
colors = ("red", "green", "blue")
print(f"Colors: {colors}")
print()

# Tuple with one item (note the comma)
print("Tuple with one item:")
one_item = ("yellow",)
print(f"One item tuple: {one_item}, type: {type(one_item)}")
print()

# Accessing items
print("3. Accessing tuple items")
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print()

# Iterating through a tuple
print("4. Looping through a tuple")
for color in colors:
    print(f"- {color}")
print()

# Tuple methods
print("5. Tuple methods: count(), index()")
numbers = (1, 2, 3, 2, 4, 2)
print(f"Numbers tuple: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 4: {numbers.index(4)}")
print()

# Tuples are immutable
print("6. Tuples are immutable (this will cause an error if uncommented)")
print("# colors[0] = 'purple'  # TypeError: 'tuple' object does not support item assignment")
print()

# Tuples vs Lists
print("7. Tuples vs Lists")
print("- Tuples are faster and use less memory.")
print("- Use tuples when data should not change.")
print("- Use lists when data needs to be updated frequently.")
print()

# Nested tuples
print("8. Nested tuples")
person = ("Alice", 30, ("Engineer", "Colombia"))
print(f"Person tuple: {person}")
print(f"Job info: {person[2]}")
print()

# Interactive example
print("*" * 40)
print("|     INTERACTIVE TUPLE PRACTICE     |")
print("*" * 40)

elements = input("Enter several elements separated by commas => ")
tuple_elements = tuple(elements.split(","))
print(f"\nHere's your tuple: {tuple_elements}")
print(f"Number of elements: {len(tuple_elements)}")

item_to_check = input("Enter an item to check if it's in your tuple => ")
if item_to_check in tuple_elements:
    print(f"'{item_to_check}' is in the tuple!")
else:
    print(f"'{item_to_check}' is not in the tuple.")
