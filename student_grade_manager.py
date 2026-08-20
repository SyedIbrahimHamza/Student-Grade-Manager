student = []
while True:
    print("\n=== STUDENT GRADE MANAGER ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by Roll Number")
    print("4. Search by Name")
    print("5. Class Report (Topper, Average, Fail List)")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")
    while choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid choice. Please enter a number between 1 and 7.")
        choice = input("Enter your choice (1-7): ")

    if choice == '1':
        roll_number = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = []
        for i in range(5):
            mark = float(input(f"Enter marks for subject {i + 1}: "))
            marks.append(mark)
        student.append({'roll_number': roll_number, 'name': name, 'marks': marks})
        print("Student added successfully.")

    if choice == '2':
        if not student:
            print("No students found.")
        else:
            print("\n=== All Students ===")
            for s in student:
                print(f"Roll Number: {s['roll_number']}, Name: {s['name']}, Marks: {s['marks']}")

    if choice == '3':
        roll_number = input("Enter Roll Number to search: ")
        found = False
        for s in student:
            if s['roll_number'] == roll_number:
                print(f"Roll Number: {s['roll_number']}, Name: {s['name']}, Marks: {s['marks']}")
                found = True
                break
        if not found:
            print("Student not found.")
    if choice == '4':
        name = input("Enter Name to search: ")
        found = False
        for s in student:
            if s['name'].lower() == name.lower():
                print(f"Roll Number: {s['roll_number']}, Name: {s['name']}, Marks: {s['marks']}")
                found = True
        if not found:
            print("Student not found.")
    if choice == '5':
        if not student:
            print("No students found.")
        else:
            total_marks = 0
            topper = None
            fail_List = []
            for s in student:
                total = sum(s['marks'])
                total_marks += total
                if topper is None or total > sum(topper['marks']):
                    topper = s
            average = total_marks / len(student) if student else 0
            for s in student:
                if sum(s['marks']) < 25:
                    fail_List.append(s)
            print(f"\n=== Class Report ===")
            print(f"Average Marks: {average}")
            print(f"Topper: {topper['name']} with {sum(topper['marks'])} marks")
            print(f"Fail List: {', '.join([s['name'] for s in fail_List]) if fail_List else 'No failures'}")
    if choice =='6':
        roll_number = input("Enter Roll Number to delete: ")
        found = False
        for s in student:
            if s['roll_number'] == roll_number:
                student.remove(s)
                print("Student deleted sucesfully.")
                found = True
                break
            if not found:
                print("Student not found.")
                
        