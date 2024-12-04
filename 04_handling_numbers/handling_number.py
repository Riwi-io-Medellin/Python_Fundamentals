import math

print("*" * 41)
print("|       Number Handling in Python      |")
print("*" * 41)

print()
print("For handling numbers, it is important to distinguish between integers (int) and floating-point numbers (float).")
print("The variable 'numeroB' will be an integer, which means it can only contain whole numbers, without decimals.")
print("The variable 'numeroC' will allow decimal values, meaning it can contain both whole numbers and decimals.")
print("In summary, the variable 'numeroB' will be an integer, while 'numeroC' will allow decimals.")
print()

numeroB = int(input("Enter an integer for 'numeroB': "))
numeroC = float(input("Enter a decimal number for 'numeroC': "))

print()
print("Number Conversion")
print("Python allows you to convert between different types of numbers, such as integers, floats, and complex numbers.")
print()

integer_value = int(3.14)
float_value = float("3.14")

print()
print(f"Value of numeroB: {numeroB}, Type: {type(numeroB)}")
print(f"Value of numeroC: {numeroC}, Type: {type(numeroC)}")

# Other mathematical functions
print(math.sqrt(25))  # Prints the square root of 25
print(math.factorial(5))  # Prints the factorial of 5

# Mathematical constants
print(math.pi)  # Prints the value of π
print(math.e)   # Prints the value of e
