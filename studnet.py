def add_student(students):
    name = input("Enter Name: ")
    roll = int(input("Enter Roll Number: "))
    marks = int(input("Enter Marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students(students):
    if len(students) == 0:
        print("No students available.\n")
    else:
        print("\n--- Student List ---")
        for student in students:
            print("Name:", student["name"])
            print("Roll:", student["roll"])
            print("Marks:", student["marks"])
            print("-------------------")
        print()


def search_student(students):
    search_name = input("Enter name to search: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll:", student["roll"])
            print("Marks:", student["marks"])
            print()
            return

    print("Student not found.\n")


def main():
    students = []

    while True:
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Program Ended.")
            break
        else:
            print("Invalid choice. Try again.\n")


main()