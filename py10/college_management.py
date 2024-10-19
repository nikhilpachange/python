class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print("-" * 30)


class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student ID {student_id} removed successfully.")
                return
        print(f"Student ID {student_id} not found.")

    def view_students(self):
        if not self.students:
            print("No students currently registered.")
        else:
            print("List of Students:")
            for student in self.students:
                student.display_info()

def main():
    college = College()

    while True:
        print("\nCollege Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            course = input("Enter Student Course: ")
            student = Student(student_id, name, age, course)
            college.add_student(student)
        elif choice == '2':
            student_id = input("Enter Student ID to remove: ")
            college.remove_student(student_id)
        elif choice == '3':
            college.view_students()
        elif choice == '4':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
