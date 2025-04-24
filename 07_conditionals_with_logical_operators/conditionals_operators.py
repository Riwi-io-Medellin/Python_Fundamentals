print("*" * 40)
print("|  CONDITIONALS & LOGICAL OPERATORS  |")
print("*" * 40)
print()

# 1. Operators covered
print("1. Operators covered")
print("- Relational: >, <, >=, <=, ==, !=")
print("- Mathematical: +, -, *, /, //, **, %")
print()

# 2. Logical Operators
print("2. Logical Operators")
print("- and: both conditions must be True")
print("- or: at least one condition must be True")
print("- not: negates the condition")
print()

# 3. Simple examples with logical operators
print("3. Simple examples")
condition1 = True
condition2 = False

if condition1 == True and condition2 == True:
    print("FIRST FLAG")

if condition1 == True or condition2 == True:
    print("SECOND FLAG")

if not condition1 == False:
    print("THIRD FLAG")
print()

# 4. Login Example with AND
print("4. Login validation (AND example)")
user = input("User => ")
password = input("Password => ")

if user == "admin" and password == "12345":
    print("Login successful")
else:
    print("Login failed")
print()

# 5. Quarter validation with OR
print("5. Quarter validation (OR example)")
month = input("Enter a month (january, february, march) => ").lower()
if month == "january" or month == "february" or month == "march":
    print("It corresponds to the first quarter")
else:
    print("It does not belong to the first quarter")
