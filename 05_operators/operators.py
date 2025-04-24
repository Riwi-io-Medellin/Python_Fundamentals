print("*" * 34)
print("|         OPERATORS IN PYTHON        |")
print("*" * 34)
print()

# 1. Arithmetic Operators
print("1. Arithmetic Operators")
numberA = 4
numberB = 2
print(f"Addition: {numberA + numberB}")
print(f"Subtraction: {numberA - numberB}")
print(f"Multiplication: {numberA * numberB}")
print(f"Division: {numberA / numberB}")
print(f"Module: {13 % 5}")
print(f"Exponentiation: {2 ** 8}")
print()

# Increment / Decrement
print("Increment & Decrement examples")
tempNumber1 = 2
tempNumber1 += 1
print(f"Increment by 1: {tempNumber1}")

tempNumber2 = 5
tempNumber2 -= 1
print(f"Decrement by 1: {tempNumber2}")

tempNumber3 = 3
tempNumber3 += 5
print(f"Increment by 5: {tempNumber3}")

tempNumber4 = 13
tempNumber4 -= 4
print(f"Decrement by 4: {tempNumber4}")
print()

# 2. Comparison Operators
print("2. Comparison Operators")
NUMBER1 = 20
NUMBER2 = "20"
NUMBER3 = 30

print(f"10 == 10 => {10 == 10}")
print(f"10 == 14 => {10 == 14}")
print(f"2 == '2' => {2 == '2'}")
print(f"2 == int('2') => {2 == int('2')}")
print(f"NUMBER1 == int(NUMBER2) => {NUMBER1 == int(NUMBER2)}")
print(f"NUMBER1 == NUMBER3 => {NUMBER1 == NUMBER3}")

print(f"10 != 10 => {10 != 10}")
print(f"10 != 14 => {10 != 14}")
print(f"2 != '2' => {2 != '2'}")
print(f"2 != int('2') => {2 != int('2')}")

PASSWORD = "Abc123"
PASSWORD_CONFIRMATION = "ABC123"
print(f"Passwords match? => {PASSWORD != PASSWORD_CONFIRMATION}")

print(f"{NUMBER1} > {NUMBER3} => {NUMBER1 > NUMBER3}")
print(f"{NUMBER1} < {NUMBER3} => {NUMBER1 < NUMBER3}")
print(f"{NUMBER1} >= {NUMBER2} => {NUMBER1 >= int(NUMBER2)}")
print(f"{NUMBER1} <= {NUMBER3} => {NUMBER1 <= NUMBER3}")
print()

# 3. Logical Operators
print("3. Logical Operators")
height = 4.0
print(f"height >= 1.71 and type(height) == float => {height >= 1.71 and type(height) == float}")
print(f"height >= 1.71 and isinstance(height, int) => {height >= 1.71 and isinstance(height, int)}")

print(f"height >= 1.71 or isinstance(height, float) => {height >= 1.71 or isinstance(height, float)}")

variable = True
print(f"Original variable: {variable}")
print(f"Not variable: {not variable}")
