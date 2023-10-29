import os
import json
from file import File

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
        self.__fit_info["tracked"] = {}
        self.__fit_info["staged"] = {}
        self.__fit_info["commits"] = {}
        self.__fit_info["untracked"] = {}
        
        try:
            with open(file_path, "w") as json_file:
                json.dump(self.__fit_info, json_file)
        except OSError:
            print("Creation of the file %s failed" % file_path)
            return False
        
        return True
    
    def fit_get_status(self):
        """This is a method that will get the status of the system."""
        staged_state = self.__fit_info.get("staged")
        status_response = self.get_status_response()
        
        if status_response["modified"]:
            print("\nModified files:\n")
            for file_name in status_response["modified"]:
                print(file_name)
                
        if status_response["added"]:
            print("\nAdded files:\n")
            for file_name in status_response["added"]:
                print(file_name)
                
        if status_response["deleted"]:
            print("\nDeleted files:\n")
            for file_name in status_response["deleted"]:
                print(file_name)
                
        if staged_state:
            print("\nStaged files:\n")
            for file_name in staged_state:
                print(file_name)

    
    def take_snapshot(self):
        """This is a method that will take a snapshot of the current folder and return a dict with the files."""
        snapshot = {}
        fit_directory = os.path.join(os.getcwd(), ".fit")
        py_cache = os.path.join(os.getcwd(), "__pycache__")
        for root, dirs, files in os.walk(os.getcwd()):
            if root == fit_directory or root == py_cache:
                continue
            for file_name in files:
                file_path = os.path.join(root, file_name)
                snapshot[file_name] = File(
                    path=file_path,
                    name=file_name.split(".")[0],
                    extension=file_name.split(".")[-1],
                    size=os.path.getsize(file_path),
                    created_at=os.path.getctime(file_path),
                    updated_at=os.path.getmtime(file_path),
                    properties={},
                )
        return snapshot
    
    def fit_add_file(self, request_parameters):
        """This is a method that will add all the changed, including deleted files to the staged area."""
        status_response = self.get_status_response()
        if request_parameters[0] == ".":
            for file_name in status_response["modified"]:
                self.__fit_info["staged"][file_name] = self.__fit_info["tracked"][file_name]
                print("The file %s was added to the staged area!" % file_name)
            for file_name in status_response["added"]:
                self.__fit_info["staged"][file_name] = self.__fit_info["tracked"][file_name]
                print("The file %s was added to the staged area!" % file_name)
            for file_name in status_response["deleted"]:
                self.__fit_info["staged"][file_name] = self.__fit_info["tracked"][file_name]
                print("The file %s was added to the staged area!" % file_name)
        else:
            for file_name in request_parameters[1:]:
                if file_name in status_response["modified"]:
                    self.__fit_info["staged"][file_name] = status_response["modified"][file_name]
                    print("The file %s was added to the staged area!" % file_name)
                elif file_name in status_response["added"]:
                    self.__fit_info["staged"][file_name] = status_response["added"][file_name]
                    print("The file %s was added to the staged area!" % file_name)
                elif file_name in status_response["deleted"]:
                    self.__fit_info["staged"][file_name] = status_response["deleted"][file_name]
                    print("The file %s was added to the staged area!" % file_name)
                else:
                    print("The file %s is not in the system!" % file_name)
                    return False
        self.update_fit_info()

