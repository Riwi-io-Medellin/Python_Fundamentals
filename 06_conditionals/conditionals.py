print("*" * 34)
print("|         CONDITIONALS IN PYTHON        |")
print("*" * 34)
print()

# 1. Basic condition (IF)
print("1. Basic condition (IF)")
if 8 > 5:
    print("8 is greater than 5")
print()

# 2. IF - ELSE example
print("2. IF - ELSE example")
ice_cream = 'lemon'
if ice_cream == 'chocolate':
    print('Yes, it is a chocolate ice cream')
else:
    print('It is not a chocolate ice cream')
print()

# 3. IF - ELIF - ELSE chain
print("3. IF - ELIF - ELSE chain")
score = -4
if score == 0:
    print("The score is neutral")
elif score < 0:
    print(f"The score is negative {score}")
elif score > 0:
    print(f"The score is positive {score}")
else:
    print("The score is not within the parameters")
print()

# 4. Interactive conditional
print("4. Interactive example")
weather = input("What's the weather like? (sunny, rainy, cloudy) => ").lower()
if weather == "sunny":
    print("Take your sunglasses!")
elif weather == "rainy":
    print("Don't forget your umbrella!")
elif weather == "cloudy":
    print("Might be a good day for a walk.")
else:
    print("Weather not recognized, be prepared for anything!")