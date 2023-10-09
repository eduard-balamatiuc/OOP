from university import University
from file_management import File_management_system
from tum_structure import Tum_structure
import tools as ts

class Tum_system:
    """A class representing the TUM student management system."""

    def __init__(self):
        """Initializes a new instance of the Tum_system class."""
        self.tum_structures = []
        self.current_structure = None
        self.available_memory_files = []
        self.file_management_system = File_management_system()
        print("Welcome to the TUM student management system, process initialization started")

    def initialize_tum_system_structure(self):
        """Initializes the TUM system structure."""
        print("Select and type in the number of the option from below: ")
        print("    0. Use previous structure")
        print("    1. Create a new structure")
        print("    2. Exit")
        initialization_option = input()

        if initialization_option == "0":
            output_text, self.available_memory_files = ts.get_available_structure_versions(
                self.file_management_system.get_available_files()
            )
            if not output_text:
                print("There are no available files, please create a new structure")
                self.initialize_tum_system_structure()
            else:
                print("Below are provided the available systems.")
                print(output_text)
                print("Please type in the number of the system from the list that you would like to continue with")
                selected_version = input()
                self.current_structure = Tum_structure(
                    selected_file = self.available_memory_files[int(selected_version)],
                )
                self.start_tum_system_interaction()

        elif initialization_option == "1":
            self.current_structure = Tum_structure()
            self.start_tum_system_interaction()

        elif initialization_option == "2":
            self.stop_tum_system_interaction()

        else:
            print("Invalid option, please try again and use one of the provided options in the description")
            self.initialize_tum_system_structure()

    def check_system_validations(self):
        """Checks if the system is valid."""
        if not self.current_structure:
            print("No structure is initialized, starting initialization process")
            self.initialize_tum_system_structure()
        else:
            return True

    def start_tum_system_interaction(self):
        """Starts the interaction with the TUM system.
        This function displays a menu of actions that the user can perform and handles the selected action.
        """
        if self.check_system_validations():
            print("Select the type of action you would like to perform:")
            print("    0. Student actions")
            print("    1. Faculty actions")
            print("    2. University actions")
            print("    3. Save current structure")
            print("    4. Back")
            print("    5. Exit")
            action_type = input()
            if action_type == "0":
                self.student_actions()
            elif action_type == "1":
                self.faculty_actions()
            elif action_type == "2":
                self.university_actions()
            elif action_type == "3":
                self.save_current_structure()
            elif action_type == "4":
                self.initialize_tum_system_structure()
            elif action_type == "5":
                self.stop_tum_system_interaction()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
                self.start_tum_system_interaction()

    def stop_tum_system_interaction(self):
        """Stops the interaction with the TUM system.
        This function asks the user if they want to save the current structure and terminates the process accordingly.
        """
        if self.current_structure:
            print("Do you want to save the current structure?")
            print("    0. Yes")
            print("    1. No")
            save_option = input()
            if save_option == "0":
                self.save_current_structure()
            else:
                print("The current structure will not be saved")
        print("Thank you for using the TUM student management system, process terminated")

    def faculty_actions(self):
        """Handles faculty-specific actions within the TUM system.
        This function displays a menu of faculty actions that the user can perform and handles the selected action.
        """
        if self.check_system_validations():
            print("Select the type of faculty action you would like to perform:")
            print("    0. Add a student")
            print("    1. Graduate a student")
            print("    2. Display enrolled students")
            print("    3. Display graduated students")
            print("    4. Display all students")
            print("    5. Check student belonging")
            print("    6. Back")
            action_type = input()
            if action_type == "0":
                self.system_add_student()
            elif action_type == "1":
                self.system_graduate_student()
            elif action_type == "2":
                self.system_display_enrolled_students()
            elif action_type == "3":
                self.system_display_graduated_students()
            elif action_type == "4":
                self.system_display_all_students()
            elif action_type == "5":
                self.system_check_student_information()
            elif action_type == "6":
                self.start_tum_system_interaction()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
                self.faculty_actions()
      
    def university_actions(self):
        """Handles university-specific actions within the TUM system.
        This function displays a menu of university actions that the user can perform and handles the selected action.
        """
        if self.check_system_validations():
            print("Select the type of university action you would like to perform:")
            print("    0. Add a faculty")
            print("    1. Display all faculties")
            print("    2. Display faculties by field")
            print("    3. Search for a faculty by student")
            print("    4. Update faculty information")
            print("    5. Back")
            action_type = input()
            if action_type == "0":
                self.system_add_faculty()
            elif action_type == "1":
                self.system_display_all_faculties()
            elif action_type == "2":
                self.system_display_faculties_by_field()
            elif action_type == "3":
                self.system_search_faculty_by_student()
            elif action_type == "4":
                self.system_update_faculty_information()
            elif action_type == "5":
                self.start_tum_system_interaction()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
                self.university_actions()

    def student_actions(self):
        """Handles student-specific actions within the TUM system.
        This function displays a menu of student actions that the user can perform and handles the selected action.
        """
        if self.check_system_validations():
            print("Select the type of student action you would like to perform:")
            print("    0. Update student information")
            print("    1. Back")
            action_type = input()
            if action_type == "0":
                self.system_update_student_information()
            elif action_type == "1":
                self.start_tum_system_interaction()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
                self.student_actions()

    def save_current_structure(self):
        """Saves the current structure to a file.
        If there is no current structure initialized, it prompts the user to initialize a structure first.
        """
        if self.current_structure:
            self.file_management_system.save_structure_file(
                self.current_structure.selected_file,
                self.current_structure.university.to_dict(),
            )
        else:
            print("No structure is initialized, please initialize a structure first")
            self.initialize_tum_system_structure()

    def system_add_student(self):
        """Adds a student to the current structure."""
        if self.check_system_validations():
            print("Please type in the student information in the following format:")
            print("    <faculty_id>, ",
                  "<student_first_name>, ",
                  "<student_last_name>, ",
                  "<student_email>, ",
                  "<student_enrollment_date>, ",
                  "<student_graduation_status>, ",
                  "<student_birth_date>")
            student_information = input()
            self.current_structure.add_student(student_information)
        self.faculty_actions()
            
    def system_graduate_student(self):
        """Graduates a student from the current structure."""
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to graduate")
            student_id = input()
            self.current_structure.graduate_student(student_id)
        self.faculty_actions()
            
    def system_display_enrolled_students(self):
        """Displays the enrolled students from the current structure."""
        if self.check_system_validations():
            print("Below are provided the enrolled students:")
            self.current_structure.display_enrolled_students()
        self.faculty_actions()
    
    def system_display_graduated_students(self):
        """Displays the graduated students from the current structure."""
        if self.check_system_validations():
            print("Below are provided the graduated students:")
            self.current_structure.display_graduated_students()
        self.faculty_actions()
            
    def system_check_student_information(self):
        """Checks the student information from the current structure."""
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to check")
            student_id = input()
            print(self.current_structure.check_student_information(student_id))
        self.faculty_actions()
            
    def system_display_all_students(self):
        """Displays all the students from the current structure."""
        if self.check_system_validations():
            print("Below are provided all the students:")
            self.current_structure.display_all_students()
        self.faculty_actions()
            
    def system_add_faculty(self):
        """Adds a faculty to the current structure."""
        if self.check_system_validations():
            print("Please type in the faculty information in the following format:")
            print("    <faculty_name>, ",
                  "<faculty_abbreviation>, ",
                  "<faculty_field>",
            )
            faculty_information = input()
            self.current_structure.add_faculty(faculty_information)
        self.university_actions()
            
    def system_display_all_faculties(self):
        """Displays all the faculties from the current structure."""
        if self.check_system_validations():
            print("Below are provided all the faculties:")
            self.current_structure.display_all_faculties()
        self.university_actions()
        
    def system_display_faculties_by_field(self):
        """Displays the faculties by field from the current structure."""
        if self.check_system_validations():
            print("Please type in the field of the faculties you would like to display")
            field = input()
            self.current_structure.display_faculties_by_field(field)
        self.university_actions()
            
    def system_search_faculty_by_student(self):
        """Searches a faculty by student from the current structure."""
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to search for")
            student_id = input()
            self.current_structure.search_faculty_by_student(student_id)
        self.university_actions()
            
    def system_update_faculty_information(self):
        """Updates the faculty information from the current structure."""
        if self.check_system_validations():
            print("Please type in the faculty name of the faculty you would like to update")
            print("Available faculties are:")
            self.current_structure.display_all_faculties()
            faculty_id = input()
            print(self.current_structure.check_faculty_information(faculty_id))
            print("Select the information you would like to update:")
            print("    0. Faculty name")
            print("    1. Faculty abbreviation")
            print("    2. Faculty field")
            print("    3. Back")
            information_type = input()
            if information_type == "0":
                print("Please type in the new faculty name")
                faculty_name = input()
                self.current_structure.update_faculty_name(faculty_id, faculty_name)
            elif information_type == "1":
                print("Please type in the new faculty abbreviation")
                faculty_abbreviation = input()
                self.current_structure.update_faculty_abbreviation(faculty_id, faculty_abbreviation)
            elif information_type == "2":
                print("Please type in the new faculty field")
                faculty_field = input()
                self.current_structure.update_faculty_field(faculty_id, faculty_field)
            elif information_type == "3":
                self.university_actions()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
        self.university_actions()
            
    def system_update_student_information(self):
        """Updates the student information from the current structure."""
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to update")
            student_id = input()
            print(self.current_structure.check_student_information(student_id))
            print("Select the information you would like to update:")
            print("    0. Student first name")
            print("    1. Student last name")
            print("    2. Student email")
            print("    3. Student enrollment date")
            print("    4. Student graduation status")
            print("    5. Student birth date")
            print("    6. Back")
            information_type = input()
            if information_type == "0":
                print("Please type in the new student first name")
                student_first_name = input()
                self.current_structure.update_student_first_name(student_id, student_first_name)
            elif information_type == "1":
                print("Please type in the new student last name")
                student_last_name = input()
                self.current_structure.update_student_last_name(student_id, student_last_name)
            elif information_type == "2":
                print("Please type in the new student email")
                student_email = input()
                self.current_structure.update_student_email(student_id, student_email)
            elif information_type == "3":
                print("Please type in the new student enrollment date")
                student_enrollment_date = input()
                self.current_structure.update_student_enrollment_date(student_id, student_enrollment_date)
            elif information_type == "4":
                print("Please type in the new student graduation status")
                student_graduation_status = input()
                self.current_structure.update_student_graduation_status(student_id, student_graduation_status)
            elif information_type == "5":
                print("Please type in the new student birth date")
                student_birth_date = input()
                self.current_structure.update_student_birth_date(student_id, student_birth_date)
            elif information_type == "6":
                self.student_actions()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
        self.student_actions()