print("*" * 34)
print("|        DICTIONARIES IN PYTHON       |")
print("*" * 34)
print()

# What is a dictionary?
print("1. What is a dictionary?")
print("A dictionary is a collection of key-value pairs.")
print("It is unordered, mutable, and indexed by keys.")
print("Defined with curly braces { }")
print()

# Creating a dictionary
print("2. Creating a dictionary")
person = {
    "name": "Alice",
    "age": 30,
    "city": "Medellín"
}
print(f"Person: {person}")
print()

# Accessing items
print("3. Accessing values by keys")
print(f"Name: {person['name']}")
print(f"City: {person.get('city')}")
print()

# Adding and modifying items
print("4. Adding or modifying entries")
person["profession"] = "Engineer"
person["age"] = 31
print(f"Updated person: {person}")
print()

# Removing items
print("5. Removing items")
del person["city"]
removed = person.pop("profession")
print(f"Removed profession: {removed}")
print(f"After deletion: {person}")
print()

# Dictionary methods
print("6. Useful dictionary methods")
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")
print()

# Looping through dictionary
print("7. Iterating through dictionary")
for key, value in person.items():
    print(f"{key}: {value}")
print()

# Nested dictionaries
print("8. Nested dictionaries")
student = {
    "name": "Juan",
    "grades": {"math": 4.5, "science": 3.8}
}
print(f"Student info: {student}")
print(f"Math grade: {student['grades']['math']}")
print()

# Interactive section
print("*" * 42)
print("|      INTERACTIVE DICTIONARY PRACTICE     |")
print("*" * 42)

user_dict = {}
add_more = "yes"

while add_more.lower() == "yes":
    key = input("Enter a key => ")
    value = input("Enter a value => ")
    user_dict[key] = value
    add_more = input("Do you want to add another key-value pair? (yes/no) => ")

print("\nHere's your complete dictionary:")
for k, v in user_dict.items():
    print(f"{k}: {v}")
