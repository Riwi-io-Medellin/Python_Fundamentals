user = []
# Name - price - category
products = [
    ["rice lb", 4000, "groceries"],
    ["sugar lb", 4500, "groceries"],
    ["plantain lb", 1000, "vegetables"],
    ["chicken lb", 6000, "meats"],
    ["beef lb", 7500, "meats"],
    ["banana lb", 2000, "fruits"],
    ["pear lb", 3000, "fruits"],
    ["powdered soap lb", 4200, "cleaning"],
    ["tomato lb", 1500, "vegetables"],
    ["potato lb", 4000, "vegetables"]
]

cart = []

print()
print("==" * 25)
print("||              Shopping Cart              ||")
print("==" * 25)
try:
    while True:
        print("-" * 50)
        print("                      MENU                      ")
        print("-" * 50)
        print()
        print("[1] Register user or update user details")
        print("[2] Add product to shopping cart")
        print("[3] View shopping cart")
        print("[4] Update shopping cart")
        print("[5] Remove product from shopping cart")
        print("[6] Exit program")
        option = int(input("-> "))
        if option == 1:
            print("-" * 50)
            if not user:
                first_name = input("Enter your first name(s) => ")
                last_name = input("Enter your last name(s) => ")
                document = input("Enter your document number => ")

                user.append(first_name)
                user.append(last_name)
                user.append(document)

                print("User registered successfully")
            else:
                print("The user is already registered, you can edit it if you wish")
                print()
                first_name = input("Enter your first name(s) => ")
                last_name = input("Enter your last name(s) => ")
                document = input("Enter your document number => ")

                user[0] = first_name
                user[1] = last_name
                user[2] = document

                print("User updated successfully")
        elif option == 2:
            print("-" * 50)
            print("Available products")
            print("-" * 50)
            count = 0
            for i in products:
                print(f"[{count + 1}] {i[0]} - ({i[1]})")
                count += 1
            product = int(input("Enter the ID of the product you want to add => "))
            product = (product - 1)
            print(f"    How many units of '{products[product][0]}' do you want?")
            quantity = int(input("(e.g., 7) -> "))
            cart_item = []
            cart_item.append(products[product][0])
            cart_item.append(products[product][1])
            cart_item.append(quantity)
            cart_item.append((products[product][1] * quantity))
            cart_item.append(products[product][2])
            cart.append(cart_item)
            print()
            print("PRODUCT ADDED TO CART")
            print()
        elif option == 3:
            print("-" * 50)
            if not cart:
                print("The cart is empty")
            else:
                print("-" * 35)
                print("Current cart")
                print("-" * 35)
                subtotal = 0
                for i in cart:
                    print(f"{i[0]}({i[1]}) * {i[2]} = {i[3]}")
                    subtotal += i[3]
                print("-" * 35)
                tax = subtotal * 0.19
                total = (subtotal + tax)

                print("SUBTOTAL =", subtotal)
                print("TAX 19% =", tax)
                print("TOTAL =", total)
                print("-" * 35)
        elif option == 4:
            print("-" * 50)
            if not cart:
                print("The cart is empty")
            else:
                print("Cart")
                count = 0
                for i in cart:
                    print(f"[{count + 1}] {i[0]}({i[1]}) * {i[2]} = {i[3]}")
                    count += 1
                product = int(input("Enter the ID of the product you want to update => "))
                product = (product - 1)
                new_quantity = int(input(f"    How many units of '{cart[product][0]}' do you want? => "))
                cart[product][2] = new_quantity
                cart[product][3] = (cart[product][1] * new_quantity)
                print()
                print("PRODUCT UPDATED SUCCESSFULLY")
                print()
        elif option == 5:
            print("-" * 50)
            if not cart:
                print("The cart is empty")
            else:
                print("Cart")
                count = 0
                for i in cart:
                    print(f"[{count + 1}] {i[0]}({i[1]}) * {i[2]} = {i[3]}")
                    count += 1
                product = int(input("Enter the ID of the product you want to remove => "))
                product = (product - 1)
                del cart[product]
                print()
                print("PRODUCT REMOVED SUCCESSFULLY")
                print()
        elif option == 6:
            print("It was a pleasure serving you!")
            exit()
        else:
            print("The option is not in the menu")
except ValueError:
    print("You entered an invalid value")
