import os
from fit import Fit

class FitInteraction:
    """A class that will mimic the git functionalities with the word "fit" as the keyword"""
    def __init__(self):
        self.__state = "init"
        self.__request_parameters = []
    
    def interaction_initialization(self):
        """This is a method that will start the system and initialize it."""
        print("Welcome to the Fit system!")
        print("Type 'fit help' to see the available commands.")
        self.__state = "running"
    
    def fit_help(self):
        """This is a method that will print the help menu."""
        print("The available commands are:")
        print("fit init - to initialize the system")
        print("fit help - to see the available commands")
        print("fit status - to see the status of the system")
        print("fit add - to add a file to the system")
        print("fit commit - to commit the changes to the system")
    
        
    def fit_init(self):
        """This is a method that will initialize a fit system in the current folder."""
        if Fit.fit_check_hidden_system_folder():
            print("The system is already initialized!")
        elif Fit.fit_create_hidden_system():
            print("The system was initialized successfully!")
        else:
            print("The system could not be initialized!")
            
    def fit_status(self):
        """This is a method that will check the status of the system."""
        if not Fit.fit_check_hidden_system_folder():
            print("The system is not initialized!")
            return
        
        print(Fit.fit_get_status())

    