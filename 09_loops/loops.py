print("*" * 32)
print("|          LOOPS IN PYTHON          |")
print("*" * 32)
print()

# 1. Classic version without loops
print("1. Classic version without loops")
numberList = []
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
number4 = int(input("Enter number 4: "))
number5 = int(input("Enter number 5: "))

numberList.append(number1)
numberList.append(number2)
numberList.append(number3)
numberList.append(number4)
numberList.append(number5)
print(f"List with 5 numbers: {numberList}")
print()

# 2. Version with FOR loop
print("2. Version with FOR loop")
numberList = []
for roundNumber in range(5):
    number = int(input(f"Enter a number # {roundNumber + 1} => "))
    numberList.append(number)
print(f"List using FOR: {numberList}")
print()

# 3. Version with WHILE loop
print("3. Version with WHILE loop")
numberList = []
roundNumber = 0
while roundNumber < 5:
    number = int(input(f"Enter a number # {roundNumber + 1} => "))
    numberList.append(number)
    roundNumber += 1
print(f"List using WHILE: {numberList}")
print()

# 4. Student Registration Exercise
print("4. Student registration with WHILE loop")
studentListRiwi = []
addAnotherStudent = "yes"

while addAnotherStudent.lower() == "yes":
    print("\n--- New Student ---")
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
    addAnotherStudent = input("Do you want to add another student? (yes/no) => ")

print("\nRegistered students:")
for student in studentListRiwi:
    print(f"""
        First Name => {student['first_name']}
        Last Name => {student['last_name']}
        Age => {student['age']}
        Email => {student['email']}
        Address => {student['address']}
    """)
