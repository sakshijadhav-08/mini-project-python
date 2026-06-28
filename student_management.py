# Student Management System

students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    # Add Student
    if choice == "1":
        roll = int(input("\nEnter Roll Number: "))

        if roll in students:
            print("Roll Number Already Exists!")
        else:
            name = input("Enter Name: ")

            marks = []
            total = 0

            for i in range(1, 6):
                mark = float(input(f"Enter Marks of Subject {i}: "))
                marks.append(mark)
                total += mark

            percentage = total / 5

            if percentage >= 90:
                grade = "O"
            elif percentage >= 80:
                grade = "A+"
            elif percentage >= 70:
                grade = "A"
            elif percentage >= 60:
                grade = "B+"
            elif percentage >= 50:
                grade = "B"
            else:
                grade = "F"

            students[roll] = {
                "Name": name,
                "Marks": marks,
                "Percentage": percentage,
                "Grade": grade
            }

            print("\n=== Record Added Successfully ===")
            print("Name:", name, "| Roll:", roll, "| %:", round(percentage, 2), "| Grade:", grade)

    # View All Students
    elif choice == "2":
        if len(students) == 0:
            print("No Records Found!")
        else:
            for roll, data in students.items():
                print("\nRoll No:", roll)
                print("Name:", data["Name"])
                print("Marks:", data["Marks"])
                print("Percentage:", round(data["Percentage"], 2))
                print("Grade:", data["Grade"])

    # Search Student
    elif choice == "3":
        roll = int(input("Enter Roll Number to Search: "))

        if roll in students:
            data = students[roll]

            print("\nStudent Found")
            print("Name:", data["Name"])
            print("Marks:", data["Marks"])
            print("Percentage:", round(data["Percentage"], 2))
            print("Grade:", data["Grade"])
        else:
            print("Student Not Found!")

    # Update Student
    elif choice == "4":
        roll = int(input("Enter Roll Number to Update: "))

        if roll in students:
            name = input("Enter New Name: ")

            marks = []
            total = 0

            for i in range(1, 6):
                mark = float(input(f"Enter New Marks of Subject {i}: "))
                marks.append(mark)
                total += mark

            percentage = total / 5

            if percentage >= 90:
                grade = "O"
            elif percentage >= 80:
                grade = "A+"
            elif percentage >= 70:
                grade = "A"
            elif percentage >= 60:
                grade = "B+"
            elif percentage >= 50:
                grade = "B"
            else:
                grade = "F"

            students[roll] = {
                "Name": name,
                "Marks": marks,
                "Percentage": percentage,
                "Grade": grade
            }

            print("Record Updated Successfully!")
        else:
            print("Student Not Found!")

    # Delete Student
    elif choice == "5":
        roll = int(input("Enter Roll Number to Delete: "))

        if roll in students:
            del students[roll]
            print("Record Deleted Successfully!")
        else:
            print("Student Not Found!")

    # Exit
    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")