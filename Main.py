
# ==========================================
# STUDENT RECORD MANAGEMENT SYSTEM
# Using Python File Handling
# ==========================================


# Create the file if it does not exist
with open("students.txt", "a") as f:
    pass


# ==========================================
# 1. ADD STUDENT
# ==========================================

def add_student():
    print("\n----- ADD STUDENT -----")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")

    # Check whether the ID already exists
    with open("students.txt", "r") as f:
        for line in f:
            if line.startswith(student_id + ","):
                print("Error: Student ID already exists!")
                return

    # Add the new student to the file
    with open("students.txt", "a") as f:
        f.write(f"{student_id},{name},{marks}\n")

    print("Student added successfully!")


# ==========================================
# 2. VIEW ALL STUDENTS
# ==========================================

def view_students():
    print("\n----- ALL STUDENTS -----")

    with open("students.txt", "r") as f:
        data = f.read()

    if data == "":
        print("No student records found.")
    else:
        print("\nID, Name, Marks")
        print("-------------------------")
        print(data)


# ==========================================
# 3. SEARCH STUDENT
# ==========================================

def search_student():
    print("\n----- SEARCH STUDENT -----")

    student_id = input("Enter Student ID to search: ")
    found = False

    with open("students.txt", "r") as f:
        for line in f:
            if line.startswith(student_id + ","):
                details = line.strip().split(",")

                print("\nStudent Found!")
                print("ID:", details[0])
                print("Name:", details[1])
                print("Marks:", details[2])

                found = True
                break

    if not found:
        print("Student not found.")


# ==========================================
# 4. DELETE STUDENT
# ==========================================

def delete_student():
    print("\n----- DELETE STUDENT -----")

    student_id = input("Enter Student ID to delete: ")
    found = False

    # Read all existing records
    with open("students.txt", "r") as f:
        lines = f.readlines()

    # Rewrite the file without the selected student
    with open("students.txt", "w") as f:
        for line in lines:
            if line.startswith(student_id + ","):
                found = True
            else:
                f.write(line)

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# ==========================================
# 5. MAIN MENU
# ==========================================

while True:

    print("\n================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
