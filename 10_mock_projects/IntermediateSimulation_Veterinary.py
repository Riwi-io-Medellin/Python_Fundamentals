patients = [
    {
        "name": "Kronos",
        "breed": "Mixed breed",
        "age": 2,
        "ownerID": "3935353",
        "status": False
    },
    {
        "name": "Lucas",
        "breed": "Mixed breed",
        "age": 2,
        "ownerID": "3935353",
        "status": True
    },
    {
        "name": "Mateo",
        "breed": "Mixed breed",
        "age": 2,
        "ownerID": "3935353",
        "status": False
    },
]

while True:
    print("Daly Veterinary")
    print("""
MENU
(1) Register a new patient

(2) Update a patient

(3) List active patients

(4) List inactive patients
        
(5) List all patients

(6) Close program
    """)

    menu_option = input("ENTER AN OPTION => ")
    if menu_option == "1":
        name = input("Enter the patient's name => ")
        breed = input("Enter the patient's breed => ")
        age = int(input("Enter the patient's age => "))
        owner_id = input("Enter the owner's ID => ")
        status = input("Enter the patient's status ('True' if in the clinic or 'False' if discharged) => ")

        new_patient = {
            "name": name,
            "breed": breed,
            "age": age,
            "ownerID": owner_id,
            "status": status.lower() == "true"
        }

        patients.append(new_patient)
    elif menu_option == "2":
        index = 0
        print("PATIENTS")
        for patient in patients:
            print(f"""
                ID=[{index}]
                Name={patient["name"]}
                Breed={patient["breed"]}
                Age={patient["age"]}
                Owner ID={patient["ownerID"]}
                Status={patient["status"]}
                """)
            index += 1

        patient_to_update = int(input("Enter the ID of the patient to update => "))
        new_name = input("Enter the patient's new name => ")
        new_breed = input("Enter the patient's new breed => ")
        new_age = int(input("Enter the patient's new age => "))
        new_owner_id = input("Enter the new owner's ID => ")
        new_status = input("Enter the new status ('True' if in the clinic or 'False' if discharged) => ")

        patients[patient_to_update]["name"] = new_name
        patients[patient_to_update]["breed"] = new_breed
        patients[patient_to_update]["age"] = new_age
        patients[patient_to_update]["ownerID"] = new_owner_id
        patients[patient_to_update]["status"] = new_status.lower() == "true"
    elif menu_option == "3":
        index = 0
        print("ACTIVE PATIENTS")
        for patient in patients:
            if patient["status"]:
                print(f"""
                    ID=[{index}]
                    Name={patient["name"]}
                    Breed={patient["breed"]}
                    Age={patient["age"]}
                    Owner ID={patient["ownerID"]}
                    Status={patient["status"]}
                    """)
                index += 1
    elif menu_option == "4":
        index = 0
        print("INACTIVE PATIENTS")
        for patient in patients:
            if not patient["status"]:
                print(f"""
                    ID=[{index}]
                    Name={patient["name"]}
                    Breed={patient["breed"]}
                    Age={patient["age"]}
                    Owner ID={patient["ownerID"]}
                    Status={patient["status"]}
                    """)
                index += 1
    elif menu_option == "5":
        index = 0
        print("ALL PATIENTS")
        for patient in patients:
            print(f"""
                ID=[{index}]
                Name={patient["name"]}
                Breed={patient["breed"]}
                Age={patient["age"]}
                Owner ID={patient["ownerID"]}
                Status={patient["status"]}
                """)
            index += 1
    elif menu_option == "6":
        print("Goodbye!")
        break
    else:
        print("You entered an invalid option.")