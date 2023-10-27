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