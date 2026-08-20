# Student Grade Manager

A simple terminal-based **Student Grade Manager** built with Python. The program provides a menu-driven interface to add students, view student records, search for students, generate a basic class report, and delete student records.

## What It Does

The program currently allows you to:

* Display a menu with student management options
* Add a new student
* Store the student's roll number and name
* Take marks for 5 subjects
* Store multiple student records using a Python list
* Organize each student record using a dictionary
* View all student records
* Search for a student by roll number
* Search for a student by name
* Perform case-insensitive name searches
* Generate a class report
* Calculate total marks for each student
* Calculate the class average
* Identify the class topper
* Generate a list of students who are failing
* Delete a student by roll number
* Validate the menu choice before continuing
* Handle an empty student list

## Current Features

| Option | Feature                                   | Status         |
| ------ | ----------------------------------------- | -------------- |
| 1      | Add Student                               | ✅ Complete     |
| 2      | View All Students                         | ✅ Complete     |
| 3      | Search by Roll Number                     | ✅ Complete     |
| 4      | Search by Name                            | ✅ Complete     |
| 5      | Class Report (Topper, Average, Fail List) | ✅ Complete     |
| 6      | Delete Student                            | ✅ Complete     |
| 7      | Exit                                      | 🔄 Coming Soon |

## How to Run

Make sure Python is installed on your computer.

Run the program from the terminal:

```bash
python student_grade_manager.py
```

The program will display a menu and ask you to select an option from **1 to 7**.

## Menu

```text
=== STUDENT GRADE MANAGER ===
1. Add Student
2. View All Students
3. Search by Roll Number
4. Search by Name
5. Class Report (Topper, Average, Fail List)
6. Delete Student
7. Exit
```

The menu choice is validated using a `while` loop. If an invalid option is entered, the program asks the user to enter a number between 1 and 7.

## Add a Student

Select **1** to add a new student.

The program asks for:

* Roll number
* Student name
* Marks for 5 subjects

Example:

```text
Enter your choice (1-7): 1

Enter Roll Number: 101
Enter Name: Ali
Enter marks for subject 1: 85
Enter marks for subject 2: 78
Enter marks for subject 3: 90
Enter marks for subject 4: 88
Enter marks for subject 5: 82

Student added successfully.
```

The five marks are collected using a `for` loop and converted into numbers using `float()`.

Each student is stored as a dictionary:

```python
{
    'roll_number': '101',
    'name': 'Ali',
    'marks': [85.0, 78.0, 90.0, 88.0, 82.0]
}
```

Multiple student dictionaries are stored inside the `student` list.

## View All Students

Select **2** to display all students currently stored in the program.

Example:

```text
Enter your choice (1-7): 2

=== All Students ===
Roll Number: 101, Name: Ali, Marks: [85.0, 78.0, 90.0, 88.0, 82.0]
Roll Number: 102, Name: Ahmed, Marks: [75.0, 81.0, 79.0, 88.0, 90.0]
```

If no students have been added yet, the program displays:

```text
No students found.
```

## Search by Roll Number

Select **3** to search for a student using their roll number.

Example:

```text
Enter your choice (1-7): 3
Enter Roll Number to search: 101

Roll Number: 101, Name: Ali, Marks: [85.0, 78.0, 90.0, 88.0, 82.0]
```

The program loops through the student list and compares the entered roll number with each student's stored roll number.

A Boolean variable called `found` tracks whether a matching student exists. Once the student is found, `break` stops the search.

If no matching student exists:

```text
Student not found.
```

## Search by Name

Select **4** to search for a student by name.

The name search is **case-insensitive**.

For example, all of the following can match a student named `Ali`:

```text
Ali
ali
ALI
aLi
```

This is achieved using:

```python
if s['name'].lower() == name.lower():
```

Example:

```text
Enter your choice (1-7): 4
Enter Name to search: ali

Roll Number: 101, Name: Ali, Marks: [85.0, 78.0, 90.0, 88.0, 82.0]
```

If no matching student is found:

```text
Student not found.
```

Unlike the roll number search, the name search does not use `break`, so it can display multiple students with the same name.

## Class Report

Select **5** to generate a class report.

The class report currently provides:

* Average marks
* Class topper
* Fail list

Example:

```text
Enter your choice (1-7): 5

=== Class Report ===
Average Marks: 400.5
Topper: Ali with 423.0 marks
Fail List: No failures
```

If no students have been added yet, the program displays:

```text
No students found.
```

### Total Marks

The program calculates each student's total using Python's built-in `sum()` function:

```python
total = sum(s['marks'])
```

For example, if a student has:

```text
[85, 78, 90, 88, 82]
```

their total is:

```text
423
```

The total marks are used to calculate the class average and identify the topper.

### Class Average

The program adds the total marks of all students and divides them by the number of students:

```python
average = total_marks / len(student) if student else 0
```

The calculated value represents the average **total marks** of the class.

### Finding the Topper

The program keeps track of the student with the highest total marks.

It starts with:

```python
topper = None
```

Then each student's total is compared with the current topper:

```python
if topper is None or total > sum(topper['marks']):
    topper = s
```

At the end, the student with the highest total marks is displayed as the class topper.

### Fail List

The program checks each student's total marks:

```python
if sum(s['marks']) < 25:
    fail_List.append(s)
```

Students with a total below **25 marks** are added to the fail list.

If nobody meets the fail condition, the program displays:

```text
No failures
```

## Delete a Student

Select **6** to delete a student using their roll number.

The program asks for the roll number:

```text
Enter your choice (1-7): 6
Enter Roll Number to delete: 101

Student deleted sucesfully.
```

The program loops through the student list and compares the entered roll number with each student's roll number.

When a matching student is found, the student is removed using:

```python
student.remove(s)
```

The `found` Boolean variable is used to track whether the student was successfully deleted.

If the student cannot be found, the program is intended to display:

```text
Student not found.
```

## Data Structure

The project uses a **list of dictionaries** to store student records.

The main list is:

```python
student = []
```

Each student is stored in the following structure:

```python
{
    'roll_number': roll_number,
    'name': name,
    'marks': marks
}
```

For example:

```python
student = [
    {
        'roll_number': '101',
        'name': 'Ali',
        'marks': [85.0, 78.0, 90.0, 88.0, 82.0]
    },
    {
        'roll_number': '102',
        'name': 'Ahmed',
        'marks': [75.0, 81.0, 79.0, 88.0, 90.0]
    }
]
```

## What I Learned

While building this project, I practiced:

* Using Python lists to store multiple records
* Using dictionaries to organize student information
* Taking user input with `input()`
* Using `for` loops to collect marks
* Using `float()` to convert marks into numbers
* Using `while` loops for menu control
* Validating menu input
* Using `for` loops to search through records
* Comparing strings and roll numbers
* Performing case-insensitive searches using `.lower()`
* Using Boolean variables such as `found`
* Using `break` to stop a search
* Removing records from a list using `remove()`
* Checking whether a list is empty
* Using `sum()` to calculate total marks
* Calculating class averages
* Finding the student with the highest marks
* Creating a fail list using conditions
* Using `None` to initialize the topper variable
* Deleting student records by roll number

## Project Status

This project is currently **in progress**.

### Implemented Features

* ✅ Add students
* ✅ Store roll number, name, and marks
* ✅ Store multiple students
* ✅ View all students
* ✅ Search by roll number
* ✅ Search by name
* ✅ Case-insensitive name search
* ✅ Class report
* ✅ Total marks calculation
* ✅ Class average calculation
* ✅ Topper identification
* ✅ Fail list
* ✅ Delete student
* ✅ Menu choice validation
* ✅ Empty student list handling

### Not Yet Implemented

The following menu option is currently displayed but its functionality has not yet been implemented:

* 🔄 Exit

## Future Improvements

Planned improvements include:

* Add a proper exit option
* Validate marks before storing them
* Prevent marks below 0 or above 100
* Prevent duplicate roll numbers
* Improve error handling for invalid mark input
* Improve the delete student not-found handling
* Search students by partial name
* Display individual student percentages
* Add grades such as A, B, C, D, and F
* Improve the class report
* Improve the overall terminal interface
* Add confirmation before deleting a student

## Technologies Used

* **Python**
* Lists
* Dictionaries
* `while` loops
* `for` loops
* Conditional statements
* `input()`
* `float()`
* `sum()`
* `remove()`
* String methods
* Boolean variables
* `None`

## Author

Built as a Python practice project to learn the fundamentals of lists, dictionaries, loops, conditions, functions built into Python, user input, searching, deleting records, and basic student record management.
