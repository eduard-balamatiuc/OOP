from university import University
from file_management import File_management_system

class Tum_system:
    def __init__(self):
        self.file_management_system = File_management_system

    def initialize_tum_system(self):

        print(
            """
            Initializing TUM System...
            
            Select and type in the number of the option from below: 
            0. Use previous system
            1. Create a new system
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
            self.file_management_system.get_available_versions(show = True)
            print(
                """
                Please type in the number of the system in the list that you would like to continue with
                """
            )
            selected_version = input()

            self.tum = University()
            
            self.tum.load_university(input = selected_version)
            
        elif initialization_option == "1":
            self.tum = University()
        else:
            print("Invalid option, please try again and use one of the provided options in the description")

            self.initialize_tum_system()
        
