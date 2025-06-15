# student_data.py

students = []  #

"""
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = float(input("Enter student grade: "))
    students.append({"name": name, "age": age, "grade": grade})
    print("Student added!\n")

"""
    TODO: Loop through the students list and print each student's info.
    """
 #view student list
def view_students():
    if not students:
        print("No students found.")
        return
    for s in students: #loop through the student
        print(f"{s['name']} - Age: {s['age']}, Grade: {s['grade']}")

# Return the average grade of all students
def get_average_grade():
    if not students:
        print("No grades available.")
        return
    avg = sum(s["grade"] for s in students) / len(students)
    print(f"Average grade: {avg:.2f}")
