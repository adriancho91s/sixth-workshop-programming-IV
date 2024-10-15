from person import Worker, Student


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Create a Worker")
        print("2. Create a Student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the worker: ")
            age = int(input("Enter the age of the worker: "))
            salary = float(input("Enter the salary of the worker: "))
            worker = Worker(name, age, salary)
            print(worker.work())
        elif choice == '2':
            name = input("Enter the name of the student: ")
            age = int(input("Enter the age of the student: "))
            grade = input("Enter the grade of the student: ")
            student = Student(name, age, grade)
            print(student.study())
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
