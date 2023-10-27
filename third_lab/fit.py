import os
import json

class Fit:
    """A class structure that will mimic the git functionalities of git"""
    def __init__(self):
        self.__fit_info = {}
        self.__fit_folder_path = ""
    
    def fit_check_hidden_system_folder(self):
        """This is a method that will check if the fit system was already initialized in the hidden folder."""
        folder_name = ".fit"
        folder_path = os.path.join(os.getcwd(), folder_name)
        
        if os.path.exists(folder_path):
            self.__fit_folder_path = folder_path
            with open(os.path.join(self.__fit_folder_path, "fit_info.json"), "r") as json_file:
                self.__fit_info = json.load(json_file)
            return True
        else:
            return False
        
    def fit_create_hidden_system(self):
        """This is a metho that will create the hidden folder for the fit system."""
        folder_name = ".fit"
        self.__fit_folder_path = os.path.join(os.getcwd(), folder_name)
        
        try:
            os.mkdir(self.__fit_folder_path)
        except OSError:
            print("Creation of the directory %s failed" % self.__fit_folder_path)
            return False
        
        # create the commit history json file in the hidden folder
        file_name = "fit_info.json"
        file_path = os.path.join(self.__fit_folder_path, file_name)
        
        try:
            open(file_path, 'w').close()
        except OSError:
            print("Creation of the file %s failed" % file_path)
            return False
        
        return True
    
    def fit_get_status():
        """This is a method that will get the status of the system."""
        
    
    def fit_add_file(request_parameters):
        pass
    
    def fit_commit_changes(request_parameters):
        pass
    
    def fit_info_about_files(request_parameters):
        pass
    