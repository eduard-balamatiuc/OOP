from university import University

def main():
    """This is the main function of the TUM student management system"""
    print("Welcome to the TUM student management system")
    university = University()

    while True:
        print("\nTUM Board Command Menu:")
        print("Faculty Operations:")
        print("1. Create and assign a student to a faculty.")
        print("2. Graduate a student from a faculty.")
        print("3. Display current enrolled students (Graduates would be ignored).")
        print("4. Display graduates (Currently enrolled students would be ignored).")
        print("5. Check if a student belongs to a faculty.")
        print("\nGeneral Operations:")
        print("6. Create a new faculty.")
        print("7. Search what faculty a student belongs to by email.")
        print("8. Display University faculties.")
        print("9. Display all faculties belonging to a field.")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "":
            # Create and assign a student to a faculty
            # Implement this operation by taking input for student details and faculty assignment.

        elif choice == "2":
            # Graduate a student from a faculty
            # Implement this operation by taking input for student details and performing graduation.

        elif choice == "3":
            # Display current enrolled students
            # Implement this operation by iterating through faculties and displaying enrolled students.

        elif choice == "4":
            # Display graduates
            # Implement this operation by iterating through faculties and displaying graduated students.

        elif choice == "5":
            # Check if a student belongs to a faculty
            # Implement this operation by taking input for student details and checking faculty membership.

        elif choice == "6":
            # Create a new faculty
            # Implement this operation by taking input for faculty details and creating a new faculty.

        elif choice == "7":
            # Search what faculty a student belongs to by email
            # Implement this operation by taking input for a student's email and finding the faculty.

        elif choice == "8":
            # Display University faculties
            university.display_all_faculties()

        elif choice == "9":
            # Display all faculties belonging to a field
            field = input("Enter the study field (e.g., FOOD_TECHNOLOGY): ")
            faculties = university.get_faculties_by_field(field)
            for faculty in faculties:
                print(f"Faculty: {faculty.name} ({faculty.abbreviation})")

        elif choice == "0":
            print("Exiting TUM Board.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
