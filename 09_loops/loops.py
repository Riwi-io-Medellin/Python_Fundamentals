numberList = []

# # CLASSIC VERSION
# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))
# number3 = int(input("Enter number 3: "))
# number4 = int(input("Enter number 4: "))
# number5 = int(input("Enter number 5: "))

# numberList.append(number1)
# numberList.append(number2)
# numberList.append(number3)
# numberList.append(number4)
# numberList.append(number5)

# for counter in range(5):
#     number = int(input("Enter a number: "))
#     numberList.append(number)

# # VERSION WITH FOR LOOP
# for roundNumber in range(5):
#     number = int(input(f"Enter a number # {roundNumber} => "))
#     numberList.append(number)

# print(numberList)

# # VERSION WITH WHILE LOOP
roundNumber = 6
while roundNumber != 6:
    number = int(input(f"Enter a number # {roundNumber} => "))
    numberList.append(number)
    
    roundNumber += 1

# Student Exercises
studentListRiwi = []

addAnotherStudent = "yes"
while addAnotherStudent == "yes":
    print("New student")
    firstName = input("Enter first name => ")
    lastName = input("Enter last name => ")
    age = input("Enter age => ")
    address = input("Enter address => ")
    email = input("Enter email => ")

    student = {
        "first_name": firstName,
        "last_name": lastName,
        "age": age,
        "address": address,
        "email": email
    }
    
    studentListRiwi.append(student)
    response = input("Are you going to add another student? => ")
    
    if response != "yes":
        addAnotherStudent = False

for student in studentListRiwi:
    print(f"""
        First Name => {student["first_name"]}
        Last Name => {student["last_name"]}
        Age => {student["age"]}
        Email => {student["email"]}
        Address => {student["address"]}
    """)
