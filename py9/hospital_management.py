class Patient:
    def __init__(self, patient_id, name, age, ailment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.ailment = ailment

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Ailment: {self.ailment}")
        print("-" * 30)


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added successfully.")

    def remove_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                print(f"Patient ID {patient_id} removed successfully.")
                return
        print(f"Patient ID {patient_id} not found.")

    def view_patients(self):
        if not self.patients:
            print("No patients currently registered.")
        else:
            print("List of Patients:")
            for patient in self.patients:
                patient.display_info()

def main():
    hospital = Hospital()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Remove Patient")
        print("3. View All Patients")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            ailment = input("Enter Patient Ailment: ")
            patient = Patient(patient_id, name, age, ailment)
            hospital.add_patient(patient)
        elif choice == '2':
            patient_id = input("Enter Patient ID to remove: ")
            hospital.remove_patient(patient_id)
        elif choice == '3':
            hospital.view_patients()
        elif choice == '4':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
