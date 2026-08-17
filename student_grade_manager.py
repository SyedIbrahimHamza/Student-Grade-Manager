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