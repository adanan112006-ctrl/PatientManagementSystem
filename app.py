patients = []

try:
    file = open("patients.txt", "r")

    for line in file:
        line = line.strip()

        parts = line.split(",")

        patient = {
            "name": parts[0],
            "age": int(parts[1])
        }

        patients.append(patient)

    file.close()
    

except FileNotFoundError:
    pass

while True:
    print("\n=== Patient Management System ===")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Delete Patient")
    print("4. search Patient")
    print("5. Save Patients")
    print("6. Exit")

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

        for i in range(len(patients)):
            print(f"{i+1}. Name:{patients[i]['name']} | Age: {patients[i]['age']}")

    elif choice == "3":
        print("\npatients")
        
        for i in range(len(patients)):
            print(i + 1, patients[i]["name"] )

        delete_number = int(input("Enter Patient number to delete: "))
        del patients[delete_number -1]

        print("Patient deleted successfully!")

    elif choice == "4":
        search_name = input("Enter name to search: ")

        found = False

        for patient in patients:
            if patient["name"] == search_name:
                print("\n Found:")
                print(f"Name:{patient['name']} | Age:{patient['age']}")
                found = True
                break

        if not found:
            print("Patient not found")


    elif choice == "5":
        file = open("patients.txt", "w")

        for patient in patients:
            file.write(f"{patient['name']},{patient['age']}\n")

        file.close()

        print("patients saved successfully!")



    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")