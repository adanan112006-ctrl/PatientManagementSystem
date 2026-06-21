patients = []

while True:
    print("\n=== Patient Management System ===")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Patient")

        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))

        patient = {
            "name": name,
            "age": age
        }

        patients.append(patient)

        print("Patient added successfully!")

    elif choice == "2":
        print("\nPatients:")

        for patient in patients:
            print(patient["name"], patient["age"],)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")