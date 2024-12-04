# ######################
# ARITHMETIC OPERATORS
# ######################

numberA = 4
numberB = 2

# Addition operator (+)
print(numberA + numberB)  # 6

# Subtraction operator (-)
print(numberA - numberB)  # 2

# Multiplication operator (*)
print(numberA * numberB)  # 8

# Division operator (/)
print(numberA / numberB)  # 2.0

# Returns the remainder of a division (%)
print(13 % 5)  # 3

# Exponentiation of two numbers
print(2 ** 8)  # 256

# Increment by one unit
tempNumber1 = 2
tempNumber1 += 1
print(tempNumber1)  # 3

# Decrement by one unit
tempNumber2 = 5
tempNumber2 -= 1
print(tempNumber2)  # 4

# Increment by multiple units
tempNumber3 = 3
tempNumber3 += 5
print(tempNumber3)  # 8

# Decrement by multiple units
tempNumber4 = 13
tempNumber4 -= 4
print(tempNumber4)  # 9


# #########################
# COMPARISON OPERATORS
# #########################

NUMBER1 = 20
NUMBER2 = "20"
NUMBER3 = 30

# Equality comparison
print(10 == 10)  # True
print(10 == 14)  # False
print(2 == "2")   # False
print(2 == int("2"))  # True
print(NUMBER1 == int(NUMBER2))  # True
print(NUMBER1 == NUMBER3)  # False

# Inequality comparison
print(10 != 10)  # False
print(10 != 14)  # True
print(2 != "2")  # True
print(2 != int("2"))  # False

PASSWORD = "Abc123"
PASSWORD_CONFIRMATION = "ABC123"

print(PASSWORD != PASSWORD_CONFIRMATION)  # True

# Greater than operator
print(f"Is {NUMBER1} greater than {NUMBER3}? => {NUMBER1 > NUMBER3}")  # False

# Less than operator
print(f"Is {NUMBER1} less than {NUMBER3}? => {NUMBER1 < NUMBER3}")  # True

# Greater than or equal to, or less than or equal to
print(f"Is {NUMBER1} greater than or equal to {NUMBER2}? => {NUMBER1 >= int(NUMBER2)}")  # True
print(f"Is {NUMBER1} less than or equal to {NUMBER3}? => {NUMBER1 <= NUMBER3}")  # True


# #####################
# LOGICAL OPERATORS
# #####################

# AND operator (and)
height = 4.0
print(height >= 1.71 and type(height) == float)  # True
print(height >= 1.71 and isinstance(height, int))  # False

# OR operator (or)
print(height >= 1.71 or isinstance(height, float))  # True

# NOT operator (not)
variable = True
print(variable)  # True
print(not variable)  # False
