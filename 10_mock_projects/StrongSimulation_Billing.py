products = (
    {
        "name": "bread",
        "price": 1000
    },
    {
        "name": "cookie",
        "price": 800
    },
    {
        "name": "flour",
        "price": 1500
    }
)

customer_document = ""
customer_first_name = ""
customer_last_name = ""
invoice = []

while True:
    print()
    print("########")
    print("--MENU--")
    print("########")
    menu = """
    (1) Register customer  
    (2) Add a new product to the invoice  
    (3) List current products in the invoice  
    (4) Show invoice  
    (5) Exit the program
    """
    print(menu)

    menu_option = input("ENTER AN OPTION => ")

    if menu_option == "1":
        if customer_document == "" or customer_first_name == "" or customer_last_name == "":
            print("-------------------")
            print("Let's register you")
            customer_document = input("Enter your document number => ")
            customer_first_name = input("Enter your first name => ")
            customer_last_name = input("Enter your last name => ")
            print("-------------------")
            print("Data registered")
            print("DOC:", customer_document)
            print("FIRST NAME:", customer_first_name)
            print("LAST NAME:", customer_last_name)
        else:
            print("-------------------")
            print("A user is already registered")
            print("DOC:", customer_document)
            print("FIRST NAME:", customer_first_name)
            print("LAST NAME:", customer_last_name)
            print("Are you sure you want to update it?")
            response = input("(1) Yes (2) No => ")
            if response == "1":
                customer_document = input("Enter your document number => ")
                customer_first_name = input("Enter your first name => ")
                customer_last_name = input("Enter your last name => ")
                print("Data registered")
                print("DOC:", customer_document)
                print("FIRST NAME:", customer_first_name)
                print("LAST NAME:", customer_last_name)
                print("User updated")
    elif menu_option == "2":
        # List available products
        index = 0
        for product in products:
            print(f"[{index}] {product['name']} {product['price']}")
            index += 1
        # Ask the user to select a product to add to the invoice
        selected_product = int(input("Enter the index of the product you want to add => "))
        quantity = int(input("How many units will you buy? => "))
        total_product_price = quantity * products[selected_product]["price"]

        # Create a new dictionary to store the product in the invoice
        new_invoice_item = {
            "name": products[selected_product]["name"],
            "price": products[selected_product]["price"],
            "units": quantity,
            "total_price": total_product_price
        }
        invoice.append(new_invoice_item)
        print("Product added to the invoice")
    elif menu_option == "3":
        total_invoice_value = 0
        for product in invoice:
            total_invoice_value += product["total_price"]

        print("INVOICE")
        print("Registered data")
        print("DOC:", customer_document)
        print("FIRST NAME:", customer_first_name)
        print("LAST NAME:", customer_last_name)
        for product in invoice:
            print(f"{product['name']} {product['price']}")

        print("--------------------")
        print(total_invoice_value)

        product_count = len(invoice)
        net_value = 0
        for product in invoice:
            net_value += product["total_price"]
        tax_iva = net_value * 0.19
        total_invoice = net_value + tax_iva
        print("--------------------")
        print("Products in invoice")
        print("--------------------")
        for product in invoice:
            print(f"{product['name']} {product['price']} * {product['units']} = {product['total_price']}")
        print("--------------------")
    elif menu_option == "4":
        # Add logic to show the detailed invoice
        pass
    elif menu_option == "5":
        print("Have a great day!")
        break
    else:
        print("#############################")
        print("Invalid option, please try again")
        print("#############################")
