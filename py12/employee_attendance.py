class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.attendance = []

    def mark_attendance(self, date):
        self.attendance.append(date)
        print(f"Attendance marked for {self.name} on {date}.")

    def display_attendance(self):
        print(f"\nAttendance Record for {self.name} (ID: {self.employee_id}):")
        if not self.attendance:
            print("No attendance records found.")
        else:
            for date in self.attendance:
                print(date)
        print("-" * 30)


class AttendanceSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.employee_id] = employee
        print(f"Employee {employee.name} added successfully.")

    def mark_employee_attendance(self, employee_id, date):
        employee = self.employees.get(employee_id)
        if employee:
            employee.mark_attendance(date)
        else:
            print(f"Employee ID {employee_id} not found.")

    def view_employee_attendance(self, employee_id):
        employee = self.employees.get(employee_id)
        if employee:
            employee.display_attendance()
        else:
            print(f"Employee ID {employee_id} not found.")


def main():
    attendance_system = AttendanceSystem()

    while True:
        print("\nEmployee Attendance System")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            employee = Employee(employee_id, name)
            attendance_system.add_employee(employee)
        elif choice == '2':
            employee_id = input("Enter Employee ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            attendance_system.mark_employee_attendance(employee_id, date)
        elif choice == '3':
            employee_id = input("Enter Employee ID: ")
            attendance_system.view_employee_attendance(employee_id)
        elif choice == '4':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
