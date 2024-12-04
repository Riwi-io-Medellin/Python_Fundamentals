print()
print("="*46)
print("|| BMI (Body Mass Index) Calculator ||")
print("="*46)

name = input("Please enter your name => ").title().strip()
weight = float(input("Weight in kg (e.g., 74) => "))
height = round(float(input("Height in meters (e.g., 1.80) => ")), 2)

BMI = weight / (height * height)
BMI = round(BMI, 2)
print()
if BMI < 18.5:
    print(f"{name}, your Body Mass Index is {BMI}, which means you are 'underweight'")
elif 18.5 <= BMI <= 24.9:
    print(f"{name}, your Body Mass Index is {BMI}, which means you are 'normal weight'")
elif 25 <= BMI <= 29.9:
    print(f"{name}, your Body Mass Index is {BMI}, which means you are 'overweight'")
elif 30 <= BMI <= 34.9:
    print(f"{name}, your Body Mass Index is {BMI}, which means you have 'obesity I'")
elif 35 <= BMI <= 39.9:
    print(f"{name}, your Body Mass Index is {BMI}, which means you have 'obesity II'")
elif 40 <= BMI <= 49.9:
    print(f"{name}, your Body Mass Index is {BMI}, which means you have 'obesity III'")
elif BMI >= 50:
    print(f"{name}, your Body Mass Index is {BMI}, which means you have 'obesity IV'")