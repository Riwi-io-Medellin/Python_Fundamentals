print("")
print("#" * 18)
print("OPERATORS COVERED")
print("#" * 18)
print("relational (>, <, >=, <=, ==, !=)")
print("mathematical (+, -, *, /, //, **, %)")
print("")

print("")
print("#" * 18)
print("LOGICAL OPERATORS")
print("#" * 18)
print("logical (and, or, and not)")
print("These operators are primarily used in conditional structures to group several simple conditions.")
print("")

condition1 = True
condition2 = False

if condition1 == True and condition2 == True:
    print("FIRST FLAG")

if condition1 == True or condition2 == True:
    print("SECOND FLAG")

if not condition1 == False:
    print("THIRD FLAG")

# AND EXAMPLE
user = input("User => ")
password = input("Password => ")

if user == "admin" and password == "12345":
    print("login successful")
else:
    print("login failed")

# OR EXAMPLE
print("check if a month is in the first quarter of the year")
month = input("Month => ")
if month == "January" or month == "February" or month == "March":
    print("It corresponds to the first quarter")
