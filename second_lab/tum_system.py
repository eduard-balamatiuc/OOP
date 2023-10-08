from university import University
from file_management import File_management_system
from tum_structure import Tum_structure
import tools as ts

class Tum_system:
    def __init__(self):
        self.tum_structures = []
        self.current_structure = None
        self.available_memory_files = []
        self.file_management_system = File_management_system

    def initialize_tum_system(self):

        print(
            """
            Initializing TUM System...
            
            Select and type in the number of the option from below: 
            0. Use previous structure
            1. Create a new structure
            """
        )

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
            print(
                output_text,
                """
                Please type in the number of the system from the list that you would like to continue with
                """
            )
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
        pass
        