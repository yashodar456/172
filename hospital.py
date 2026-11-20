class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display(self):
        print(f"\nPatient ID : {self.patient_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Disease    : {self.disease}")


patients = {}

while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        pid = input("Patient ID: ")
        name = input("Patient Name: ")
        age = int(input("Patient Age: "))
        disease = input("Disease: ")

        patients[pid] = Patient(pid, name, age, disease)

        print("Patient Added Successfully")

    elif choice == "2":

        if not patients:
            print(" No Patients Found")
        else:
            for patient in patients.values():
                patient.display()

    elif choice == "3":
        pid = input("Enter Patient ID: ")

        if pid in patients:
            patients[pid].display()
        else:
            print(" Patient Not Found")

    elif choice == "4":
        pid = input("Enter Patient ID to Delete: ")

        if pid in patients:
            del patients[pid]
            print("Patient Record Deleted")
        else:
            print(" Patient Not Found")

    elif choice == "5":
        print(" Thank You")
        break

    else:
        print(" Invalid Choice")