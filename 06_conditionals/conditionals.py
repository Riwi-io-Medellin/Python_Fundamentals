# ###################
# CONDITIONALS IN PYTHON
# ###################

# Basic condition (IF)
if 8 > 5:
    print("8 is greater than 5")  # 8 is greater than 5

# Normal condition (IF - ELSE)
ice_cream = 'lemon'
if ice_cream == 'chocolate':
    print('Yes, it is a chocolate ice cream')
else:
    print('It is not a chocolate ice cream')  # It is not a chocolate ice cream

# Advanced condition (IF - ELIF - ELSE)
score = -4
if score == 0:
    print("The score is neutral")
elif score < 0:
    print(f"The score is negative {score}")  # The score is negative -4
elif score > 0:
    print(f"The score is positive {score}")
else:
    print("The score is not within the parameters")
