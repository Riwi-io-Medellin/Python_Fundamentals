print("*" * 34)
print("|     VARIABLE TYPES IN PYTHON       |")
print("*" * 34)
print()

# 1. Introduction to Variable Types
print("1. Introduction to Variable Types")
print("Python has different types of variables depending on the kind of data they store.")
print("Here are the most common types:")
print("- Integer (int): Whole numbers, e.g., 100, 260")
print("- Float (float): Numbers with decimals, e.g., 1.24, 5.7")
print("- String (str): Text, e.g., 'Hello', 'Python'")
print("- Boolean (bool): Logical values True or False")
print()

# 2. Declaring variables
print("2. Declaring variables")
integer_variable = 10
real_variable = 54.8
string_variable = "A very special greeting to all the coders"
boolean_variable = True
print(f"Integer variable: {integer_variable}")
print(f"Float variable: {real_variable}")
print(f"String variable: {string_variable}")
print(f"Boolean variable: {boolean_variable}")
print()

# 3. Checking types with type()
print("3. Checking variable types")
print(f"Type of integer_variable: {type(integer_variable)}")
print(f"Type of real_variable: {type(real_variable)}")
print(f"Type of string_variable: {type(string_variable)}")
print(f"Type of boolean_variable: {type(boolean_variable)}")
print()

# 4. Type Conversion
print("4. Type Conversion")
int_from_float = int(real_variable)
float_from_string = float("3.1416")
string_from_int = str(integer_variable)
bool_from_zero = bool(0)
print(f"int from float: {int_from_float}")
print(f"float from string: {float_from_string}")
print(f"string from int: {string_from_int}")
print(f"bool from 0 (should be False): {bool_from_zero}")
print()

# 5. Interactive Practice
print("*" * 40)
print("|     INTERACTIVE VARIABLE PRACTICE     |")
print("*" * 40)

user_input = input("Enter a number => ")
if user_input.isdigit():
    number = int(user_input)
    print(f"You entered the integer: {number}")
    print(f"Is it even? => {number % 2 == 0}")
else:
    print("That is not a valid integer!")
