coders = [
    {
        "name": "Javier",
        "age": 25,
        "riwipoints": 4
    },
    {
        "name": "Lucas",
        "age": 18,
        "riwipoints": 8
    },
    {
        "name": "Pablo",
        "age": 30,
        "riwipoints": 5
    },
    {
        "name": "Judas",
        "age": 19,
        "riwipoints": 0
    },
    {
        "name": "Mateo One",
        "age": 36,
        "riwipoints": 9
    }
]

while True:
    print("""
    MENU
    (1) Register a new coder

    (2) Update coder

    (3) Delete coder

    (4) List coders

    (5) Close program
    """)

    menu_option = input("ENTER AN OPTION => ")
    if menu_option == "1":
        name = input("Enter the coder's name => ")
        age = int(input("Enter the coder's age => "))
        riwipoints = int(input("Enter the coder's RIWIPOINTS => "))

        new_coder = {
            "name": name,
            "age": age,
            "riwipoints": riwipoints
        }

        coders.append(new_coder)
    elif menu_option == "2":
        index = 0
        for coder in coders:
            # Display coder information
            print(f"""
                ID=[{index}]
                Name={coder["name"]}
                Age={coder["age"]}
                RIWIPOINTS={coder["riwipoints"]}
                """)
            index += 1

        # Request new data
        coder_to_update = int(input("Enter the ID of the coder you want to update => "))
        new_name = input("Enter the new name for the coder => ")
        new_age = int(input("Enter the new age for the coder => "))
        new_riwipoints = int(input("Enter the new RIWIPOINTS for the coder => "))

        # Update the coder's data
        coders[coder_to_update]["name"] = new_name
        coders[coder_to_update]["age"] = new_age
        coders[coder_to_update]["riwipoints"] = new_riwipoints
    elif menu_option == "3":
        index = 0
        for coder in coders:
            print(f"ID=[{index}] - {coder['name']}")
            index += 1

        coder_to_delete = int(input("Enter the ID of the coder you want to delete => "))
        del coders[coder_to_delete]
    elif menu_option == "4":
        print("List of coders:")
        for coder in coders:
            print(f"""
                CODER NAME = {coder["name"]}
                AGE = {coder["age"]}
                RIWIPOINTS = {coder["riwipoints"]}
                """)
    elif menu_option == "5":
        print("Closing the program")
        break
    else:
        print("You entered an invalid option")
