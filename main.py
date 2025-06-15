# main.py

from student_data import add_student, view_students, get_average_grade

def main():
    print("Welcome to the Student Record System")

    while True:
        print("\n1. Add student")
        print("2. View students")
        print("3. Get average grade")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_student()  # This updates the list inside student_data.py
        elif choice == '2':
            view_students()  # This uses the updated list
        elif choice == '3':
            get_average_grade()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
