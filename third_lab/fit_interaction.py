import os
import threading
import time
from fit import Fit

class FitInteraction:
    """A class that will mimic the git functionalities with the word "fit" as the keyword"""
    def __init__(self):
        self.__state = "init"
        self.__request = ""
        self.__request_parameters = []
        self.__Fit = Fit()
    
    def interaction_initialization(self):
        """This is a method that will start the system and initialize it."""
        print("Welcome to the Fit system!")
        print("Type 'fit help' to see the available commands.")
        self.__state = "running"
        self.run()
    
    def get_request(self):
        """This is a method that will get the request from the user."""
        self.__request = input(">>>")
        self.__request_parameters = self.__request.split(" ", 2)
        
    def interaction_running(self):
        """This is a method that will keep the system running."""
        while self.__state == "running":
            # First thread does the simple system interaction
            self.get_request()
            
            if self.__request_parameters[0] == "fit":
                self.__request_parameters.pop(0)
            
            if self.__request_parameters[0] == "help":
                self.fit_help()
                print()
            elif self.__request_parameters[0] == "init":
                self.fit_init()
                print()
            elif self.__request_parameters[0] == "status":
                self.fit_status()
                print()
            elif self.__request_parameters[0] == "add":
                self.fit_add()
                print()
            elif self.__request_parameters[0] == "commit":
                self.fit_commit()
                print()
            elif self.__request_parameters[0] == "info":
                self.fit_info()
                print()
            elif self.__request_parameters[0] == "exit":
                self.__state = "exit"
                print()
            else:
                print("The command is not recognized!\n")
            
    def file_change_checker(self):
        while self.__state == "running":
            # Second thread checks every 5 seconds if any file changed and notifies the user about it
            stat_dict = self.__Fit.get_status_response_dict()
            
            if not stat_dict:
                continue
            else:
                for file in stat_dict.get("modified"):
                    print(f"The file {file} was modified!")
                for file in stat_dict.get("deleted"):
                    print(f"The file {file} was deleted!")
                for file in stat_dict.get("created"):
                    print(f"The file {file} was created!")
                print()
            time.sleep(5)

    def run(self):
        """This is method that will run in 2 threads the file change checker and interaction running"""
        f1 = threading.Thread(target=self.file_change_checker)
        f2 = threading.Thread(target=self.interaction_running)
        f1.start()
        f2.start()
        f1.join()
        f2.join()
        print("The system was closed!")
        
    def fit_help(self):
        """This is a method that will print the help menu."""
        print("The available commands are:")
        print("fit init - to initialize the system")
        print("fit help - to see the available commands")
        print("fit status - to see the status of the system")
        print("fit add - to add a file to the system")
        print("fit commit - to commit the changes to the system")
        print("fit info - to print the info about the files")
    
        
    def fit_init(self):
        """This is a method that will initialize a fit system in the current folder."""
        if self.__Fit.fit_check_hidden_system_folder():
            print("The system is already initialized!")
        elif self.__Fit.fit_create_hidden_system():
            print("The system was initialized successfully!")
        else:
            print("The system could not be initialized!")
            
    def fit_status(self):
        """This is a method that will check the status of the system."""
        if not self.__Fit.fit_check_hidden_system_folder():
            print("The system is not initialized!")
            return
        
        self.__Fit.fit_get_status()
        
    def fit_add(self):
        """This is a method that will add a file to the system."""
        if not self.__Fit.fit_check_hidden_system_folder():
            print("The system is not initialized!")
            return
        
        if self.__Fit.fit_add_file(self.__request_parameters):
            print("The files were added successfully!")
            
    def fit_commit(self):
        """This is a method that will commit the changes to the system."""
        if not self.__Fit.fit_check_hidden_system_folder():
            print("The system is not initialized!")
            return
        
        if self.__Fit.fit_commit_changes(self.__request_parameters):
            print("The changes were committed successfully!")
        else:
            print("The changes could not be committed!")
            
    def fit_info(self):
        """This is a method that will print the info about the files"""
        if not self.__Fit.fit_check_hidden_system_folder():
            print("The system is not initialized!")
            return
        
        if self.__Fit.fit_info_about_files(self.__request_parameters):
            print("The info was printed successfully!")
    