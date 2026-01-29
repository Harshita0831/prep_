#student = {"Name":"Sara", "Roll no":20, "Course":"Python"}
students = {}
while True:
    print("\n Student List")
    print("1. Add Student")
    print("2. View all Student")
    print("3. Search Students")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")
    #1. Add Student
    if choice == "1":
        roll = input("Enter Roll Number:")
        name = input("Enter Name:")
        course = input("Enter Course:")
        students[roll]={"name":name,"course":course}
        print("Student added Successfully")

    #2. View Students
    elif choice == "2":
        if students:
            print("\n All students:")
            for roll, info in students.items():
                print("Roll: ",roll)
                print("Name: ",info["name"])
                print("Course: ",info["course"])
        else:
            print("No student Record found")

    #3. Search student
    elif choice == "3":
        roll = input("Enter the roll number to search:")
        if roll in students:
            print("Name: ",students[roll]["name"])
            print("Course:", students[roll]["course"])
        else:
            print("Student not found")

    #4. delete contact
    elif choice == "4":
        roll = input("Enter Roll Number:")
        removed = students.pop(roll, "Not found")
        if removed == "not found":
            print("Student not Found")
        else:
            print("Student Deleted Successfully")
    #5. Exit
    elif choice == "5":
        print("Thank you for visiting")
        break
    else:
        print("invalid choice")
