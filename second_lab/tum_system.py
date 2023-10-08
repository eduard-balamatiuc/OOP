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
        self.is_running = True
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

                self.current_structure = Tum_structure(selected_file = self.available_memory_files[int(selected_version)])
                
        elif initialization_option == "1":
            self.current_structure = Tum_structure()
            self.start_tum_system_interaction()
            
        elif initialization_option == "2":
            self.is_running = False
            self.stop_tum_system_interaction()
            
        else:
            print("Invalid option, please try again and use one of the provided options in the description")

            self.initialize_tum_system()
            
    def check_system_validations(self):
        """ Checks if the system is valid."""
        if not self.current_structure:
            print("No structure is initialized, starting initialization process")
            self.initialize_tum_system_structure()
        else:
            return True

    def start_tum_system_interaction(self):
        """Starts the interaction with the TUM system."""
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
                self.is_running = False
                self.stop_tum_system_interaction()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
            
    def stop_tum_system_interaction(self):
        """Stops the interaction with the TUM system."""
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
                self.system_check_student_information()
            elif action_type == "5":
                self.system_display_all_students()
            elif action_type == "6":
                self.start_tum_system_interaction()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
                
    def university_actions(self):
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
    
    def student_actions(self):
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
    
    def save_current_structure(self):
        """Saves the current structure."""
        if self.current_structure:
            self.file_management_system.save_structure_file(
                self.current_structure.selected_file,
                self.current_structure.university.university_structure
            )
        else:
            print("No structure is initialized, please initialize a structure first")
            self.initialize_tum_system_structure()

    def system_add_student(self):
        """Adds a student to the current structure."""
        if self.check_system_validations():
            print("Please type in the student information in the following format:")
            print("    <student_first_name>, ",
                  "<student_last_name>, ",
                  "<student_email>, ",
                  "<student_enrollment_date>, ",
                  "<student_graduation_status>, ",
                  "<student_birth_date>")
            student_information = input()
            self.current_structure.add_student(student_information)
            
    def system_graduate_student(self):
        """Graduates a student from the current structure."""
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to graduate")
            student_id = input()
            self.current_structure.graduate_student(student_id)
            
    def system_display_enrolled_students(self):
        """Displays the enrolled students from the current structure."""
        if self.check_system_validations():
            print("Below are provided the enrolled students:")
            self.current_structure.display_enrolled_students()
    
    def system_display_graduated_students(self):
        """Displays the graduated students from the current structure."""
        if self.check_system_validations():
            print("Below are provided the graduated students:")
            self.current_structure.display_graduated_students()
            
    def system_check_student_information(self):
        """Checks the student information from the current structure."""
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to check")
            student_id = input()
            print(self.current_structure.check_student_information(student_id))
            
    def system_display_all_students(self):
        """Displays all the students from the current structure."""
        if self.check_system_validations():
            print("Below are provided all the students:")
            self.current_structure.display_all_students()
            
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
            
    def system_display_all_faculties(self):
        """Displays all the faculties from the current structure."""
        if self.check_system_validations():
            print("Below are provided all the faculties:")
            self.current_structure.display_all_faculties()
            
    def system_display_faculties_by_field(self):
        """Displays the faculties by field from the current structure."""
        if self.check_system_validations():
            print("Please type in the field of the faculties you would like to display")
            field = input()
            self.current_structure.display_faculties_by_field(field)
            
    def system_search_faculty_by_student(self):
        """Searches a faculty by student from the current structure."""
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to search for")
            student_id = input()
            self.current_structure.search_faculty_by_student(student_id)
            
    def system_update_faculty_information(self):
        """Updates the faculty information from the current structure."""
        if self.check_system_validations():
            print("Please type in the faculty name of the faculty you would like to update")
            faculty_name = input()
            print("Please type in the new faculty information in the following format:")
            print("    <faculty_name>, <faculty_field>")
            faculty_information = input()
            self.current_structure.update_faculty_information(faculty_name, faculty_information)
            
    def system_update_student_information(self):
        """Updates the student information from the current structure."""
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to update")
            student_id = input()
            print(self.current_structure.check_student_information(student_id))
            print("Select the information you would like to update:")
            print("    0. Student name")
            print("    1. Student field")
            print("    2. Student faculty")
            print("    3. Back")
            information_type = input()
            if information_type == "0":
                print("Please type in the new student name")
                student_name = input()
                self.current_structure.update_student_name(student_id, student_name)
            elif information_type == "1":
                print("Please type in the new student field")
                student_field = input()
                self.current_structure.update_student_field(student_id, student_field)
            elif information_type == "2":
                print("Please type in the new student faculty")
                student_faculty = input()
                self.current_structure.update_student_faculty(student_id, student_faculty)
            elif information_type == "3":
                self.student_actions()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")