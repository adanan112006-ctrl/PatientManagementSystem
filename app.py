patients = []

while True:
    print("\n=== Patient Management System ===")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Delete Patient")
    print("4. Exit")

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
            print(patient["name"], patient["age"])

    elif choice == "3":
        print("\npatients")
        
        for i in range(len(patients)):
            print(i + 1, patients[i]["name"] )

        delete_number = int(input("Enter Patient number to delete: "))
        del patients[delete_number -1]

        print("Patient deleted successfully!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")