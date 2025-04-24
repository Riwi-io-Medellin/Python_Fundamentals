print("*" * 30)
print("|         LISTS IN PYTHON         |")
print("*" * 30)
print()

# Creating a list
print("1. Creating a list")
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
print()

# Accessing list items
print("2. Accessing list items by index")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print()

# Modifying a list item
print("3. Modifying a list item")
fruits[1] = "blueberry"
print(f"Modified list: {fruits}")
print()

# Adding items to a list
print("4. Adding items")
fruits.append("mango")
print(f"After append: {fruits}")
fruits.insert(1, "kiwi")
print(f"After insert at index 1: {fruits}")
print()

# Removing items from a list
print("5. Removing items")
fruits.remove("cherry")
print(f"After remove: {fruits}")
popped_item = fruits.pop()
print(f"Popped item: {popped_item}")
print(f"After pop: {fruits}")
print()

# List slicing
print("6. Slicing lists")
numbers = [10, 20, 30, 40, 50, 60]
print(f"Original numbers: {numbers}")
print(f"Slice [1:4]: {numbers[1:4]}")
print(f"Last 2 items: {numbers[-2:]}")
print()

# Looping through a list
print("7. Looping through lists")
for fruit in fruits:
    print(f"- {fruit}")
print()

# Checking existence
print("8. Checking if an item exists")
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the list")
print()

# List methods
print("9. Useful list methods")
sample = [3, 1, 4, 1, 5, 9, 2]
print(f"Original list: {sample}")
print(f"Length: {len(sample)}")
sample.sort()
print(f"Sorted list: {sample}")
sample.reverse()
print(f"Reversed list: {sample}")
sample.clear()
print(f"Cleared list: {sample}")

print()
print("*" * 40)
print("|     INTERACTIVE LIST EXERCISE     |")
print("*" * 40)

user_list = []

print("Let's build your own list of favorite things!")
num_items = int(input("How many items do you want to add? => "))

for i in range(num_items):
    item = input(f"Enter item #{i+1} => ")
    user_list.append(item)

print("\nGreat! Here's your list:")
print(user_list)

print("\nNow let's explore your list!")

# View first and last item
if user_list:
    print(f"First item: {user_list[0]}")
    print(f"Last item: {user_list[-1]}")

# Check for a specific item
check_item = input("\nType an item to check if it's in your list => ")
if check_item in user_list:
    print(f"'{check_item}' is in your list!")
else:
    print(f"'{check_item}' is NOT in your list.")

# Sort and display the list
sorted_list = sorted(user_list)
print("\nYour list sorted alphabetically:")
print(sorted_list)