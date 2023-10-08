from university import University
from file_management import File_management_system
from tum_structure import Tum_structure
import tools as ts

class Tum_system:
    def __init__(self):
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
        initialization_option = input()

        if initialization_option == "0":
            print(
                """
                Below are provided the available systems.

                Please pick one that you would like to continue with  
                """
            )
            output_text, self.available_memory_files = ts.get_available_structure_versions(
                self.file_management_system.get_available_files()
            )
            if not output_text:
                print("There are no available files, please create a new structure")
                self.initialize_tum_system_structure()
            print("Below are provided the available systems.")
            print(output_text)
            print("Please type in the number of the system from the list that you would like to continue with")
            selected_version = input()

            self.current_structure = Tum_structure(selected_file = self.available_memory_files[int(selected_version)])
            
        elif initialization_option == "1":
            self.current_structure = Tum_structure()
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
            print("    4. Exit")
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
                self.is_running = False
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
            
        
    def faculty_actions(self):
        if self.check_system_validations():
            print("Select the type of faculty action you would like to perform:")
            print("    0. Add a student")
            print("    1. Graduate a student")
            print("    2. Display enrolled students")
            print("    3. Display graduated students")
            print("    4. Check student belonging")
            print("    5. Back")
            action_type = input()
            if action_type == "0":
                self.current_structure.add_student()
            elif action_type == "1":
                self.current_structure.graduate_student()
            elif action_type == "2":
                self.current_structure.display_enrolled_students()
            elif action_type == "3":
                self.current_structure.display_graduated_students()
            elif action_type == "4":
                self.current_structure.check_student_information()
            elif action_type == "5":
                self.current_structure.start_tum_system_interaction()
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
                self.current_structure.add_faculty()
            elif action_type == "1":
                self.current_structure.display_all_faculties()
            elif action_type == "2":
                self.current_structure.display_faculties_by_field()
            elif action_type == "3":
                self.current_structure.search_faculty_by_student()
            elif action_type == "4":
                self.current_structure.update_faculty_information()
            elif action_type == "5":
                self.current_structure.start_tum_system_interaction()
            else:
                print("Invalid option, please try again and use one of the provided options in the description")
    
    def student_actions(self):
        if self.check_system_validations():
            print("Select the type of student action you would like to perform:")
            print("    0. Update student information")
            print("    1. Back")
            action_type = input()
            if action_type == "0":
                self.current_structure.update_student_information()
            elif action_type == "1":
                self.current_structure.start_tum_system_interaction()
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