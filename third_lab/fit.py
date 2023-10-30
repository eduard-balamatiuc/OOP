import os
import json
from file import File, ImageFile, TextFile, CodeFile
from datetime import datetime
import secrets
import hashlib

class Fit:
    """A structure that will mimic the git functionalities of git"""
    def __init__(self):
        self.__fit_info = {}
        self.__fit_folder_path = ""
        self.__status_response = {}
        self.__old_status_response = {}
    
    def fit_check_hidden_system_folder(self):
        """This is a method that will check if the fit system was already initialized in the hidden folder."""
        folder_name = ".fit"
        folder_path = os.path.join(os.getcwd(), folder_name)
        
        if os.path.exists(folder_path):
            self.__fit_folder_path = folder_path
            with open(os.path.join(self.__fit_folder_path, "fit_info.json"), "r") as json_file:
                self.load_fit_info(json_file)
            return True
        else:
            return False
    
    def load_fit_info(self, json_file_path):
        """This is a metho that will load the fit info from the json file."""
        self.__fit_info = json.load(json_file_path)
        self.__fit_info["tracked"] = {
            file_name: File(**file_data) 
            for file_name, file_data in self.__fit_info["tracked"].items()
        }
        self.__fit_info["staged"] = {
            file_name: File(**file_data) 
            for file_name, file_data in self.__fit_info["staged"].items()
        }
        
    def get_status_response_dict(self):
        """This is a method that will return the status response dictionary if something changed from the last version."""
        if self.__status_response != self.__old_status_response:
            return self.__status_response
        else:
            return {}
        
        
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
        self.get_status_response()
        
        if self.__status_response.get("modified"):
            print("\nModified files:\n")
            for file_name in self.__status_response["modified"]:
                print(file_name)
                
        if self.__status_response.get("added"):
            print("\nAdded files:\n")
            for file_name in self.__status_response["added"]:
                print(file_name)
                
        if self.__status_response.get("deleted"):
            print("\nDeleted files:\n")
            for file_name in self.__status_response["deleted"]:
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
                file_extension = os.path.splitext(file_name)[1]
                file_size = os.path.getsize(file_path)
                file_created_at = os.path.getctime(file_path)
                file_updated_at = os.path.getmtime(file_path)
                file_properties = {}
                if file_extension in ["png", "jpg", "jpeg", "gif"]:
                    snapshot[file_name] = ImageFile(
                        path=file_path,
                        name=file_name,
                        extension=file_extension,
                        size=file_size,
                        created_at=file_created_at,
                        updated_at=file_updated_at,
                    )
                    snapshot[file_name].extract_properties()
                elif file_extension in ["txt"]:
                    snapshot[file_name] = TextFile(
                        path=file_path,
                        name=file_name,
                        extension=file_extension,
                        size=file_size,
                        created_at=file_created_at,
                        updated_at=file_updated_at,
                    )
                    snapshot[file_name].extract_properties()
                elif file_extension in ["py", "java"]:
                    snapshot[file_name] = CodeFile(
                        path=file_path,
                        name=file_name,
                        extension=file_extension,
                        size=file_size,
                        created_at=file_created_at,
                        updated_at=file_updated_at,
                    )
                    snapshot[file_name].extract_properties()
                else:
                    snapshot[file_name] = File(
                        path=file_path,
                        name=file_name,
                        extension=file_extension,
                        size=file_size,
                        created_at=file_created_at,
                        updated_at=file_updated_at,
                    )
                    
        return snapshot
    
    def fit_add_file(self, request_parameters):
        """This is a method that will add all the changed, including deleted files to the staged area."""
        self.get_status_response()
        if request_parameters[1] == ".":
            for file_name in self.__status_response.get("modified"):
                self.__fit_info.get("staged")[file_name] = self.__status_response.get("modified")[file_name]
                print("The file %s was added to the staged area!" % file_name)
                
            for file_name in self.__status_response.get("added"):
                self.__fit_info.get("staged")[file_name] = self.__status_response.get("added")[file_name]
                print("The file %s was added to the staged area!" % file_name)
                
            for file_name in self.__status_response.get("deleted"):
                self.__fit_info.get("staged")[file_name] = self.__status_response.get("deleted")[file_name]
                print("The file %s was added to the staged area!" % file_name)
        else:
            for file_name in request_parameters[1:]:
                if file_name in self.__status_response["modified"]:
                    self.__fit_info.get("staged")[file_name] = self.__status_response.get("modified")[file_name]
                    print("The file %s was added to the staged area!" % file_name)
                elif file_name in self.__status_response["added"]:
                    self.__fit_info.get("staged")[file_name] = self.__status_response.get("added")[file_name]
                    print("The file %s was added to the staged area!" % file_name)
                elif file_name in self.__status_response["deleted"]:
                    self.__fit_info.get("staged")[file_name] = self.__status_response.get("deleted")[file_name]
                    print("The file %s was added to the staged area!" % file_name)
                else:
                    print("The file %s is not in the system!" % file_name)
                    return False
        self.update_fit_info()

        
    def get_status_response(self):
        """This is a method that will provide the status response dictionary divided into 3 categories"""
        self.__old_status_response = self.__status_response
        current_state = self.take_snapshot()
        staged_state = self.__fit_info.get("staged")
        last_state = self.__fit_info.get("tracked")
        
        # Create dictionaries with file names as keys and values as values
        deleted = {file_name: last_state[file_name] 
                for file_name in last_state 
                if file_name not in current_state and file_name not in staged_state}

        added = {file_name: current_state[file_name] 
                for file_name in current_state
                if file_name not in last_state and file_name not in staged_state
                or (current_state[file_name].get_updated_at() != current_state[file_name].get_created_at())}

        modified = {file_name: last_state[file_name]
                    for file_name in current_state
                    if (file_name in last_state and file_name not in staged_state) 
                    and (last_state[file_name].get_updated_at() != current_state[file_name].get_updated_at())}
   
        self.__status_response["deleted"] = deleted
        self.__status_response["added"] = added
        self.__status_response["modified"] = modified

    def update_fit_info(self):
        """This is a method that will update the fit info json file."""
        
        file_path = os.path.join(self.__fit_folder_path, "fit_info.json")
        # convert self.__fit_info["tracked"] and self.__fit_info["staged"] to dicts
        self.__fit_info["tracked"] = {
            file_name: file_data.get_dict_data()
            for file_name, file_data in self.__fit_info["tracked"].items()
        }
        self.__fit_info["staged"] = {
            file_name: file_data.get_dict_data()
            for file_name, file_data in self.__fit_info["staged"].items()
        }
        self.__fit_info["commits"] = {
            commit_hash: commit_data
            for commit_hash, commit_data in self.__fit_info["commits"].items()
        }
        with open(file_path, "w") as json_file:
            json.dump(self.__fit_info, json_file)
            
    def fit_commit_changes(self, request_parameters):
        """This is a method that will commit the changes to the system."""
        if len(request_parameters) == 1:
            print("Please provide a commit message!")
            return False
        
        commit_hash = secrets.token_hex(16)
        commit_message = " ".join(request_parameters[1:])
        commit_time = datetime.now().timestamp()
        commit_files = {
            file_name: file_data.get_dict_data()
            for file_name, file_data in self.__fit_info["staged"].items()
        }
        
        commit = {
            "hash": commit_hash,
            "message": commit_message,
            "time": commit_time,
            "files": commit_files,
        }
        
        self.__fit_info["commits"][commit_hash] = commit
        self.__fit_info["tracked"] = {**self.__fit_info["tracked"], **self.__fit_info["staged"]}
        self.__fit_info["staged"] = {}
        self.update_fit_info()
        return True
    
    def fit_info_about_files(self, request_paramters):
        """This is a method that will print the info about the files."""
        if len(request_paramters) == 1:
            # print info about all files
            for file_name, file_data in self.take_snapshot().items():
                created_at = file_data.get_dict_data().get('created_at')
                updated_at = file_data.get_dict_data().get('updated_at')
                
                # Convert timestamps to a more human-readable format
                created_at_formatted = datetime.fromtimestamp(created_at).strftime('%Y-%m-%d %H:%M:%S')
                updated_at_formatted = datetime.fromtimestamp(updated_at).strftime('%Y-%m-%d %H:%M:%S')
                
                print(file_name)
                print(f"Created  at: {created_at_formatted}")
                print(f"Updated at: {updated_at_formatted}")
                print()
        else:
            # print info about the specified files
            for file_name in request_paramters[1:]:
                if file_name in self.take_snapshot():
                    file_data = self.take_snapshot()[file_name]
                    created_at = file_data.get_dict_data().get('created_at')
                    updated_at = file_data.get_dict_data().get('updated_at')
                    
                    # Convert timestamps to a more human-readable format
                    created_at_formatted = datetime.fromtimestamp(created_at).strftime('%Y-%m-%d %H:%M:%S')
                    updated_at_formatted = datetime.fromtimestamp(updated_at).strftime('%Y-%m-%d %H:%M:%S')
                    
                    print(file_name)
                    print(f"Created at: {created_at_formatted}")
                    print(f"Updated at: {updated_at_formatted}")
                    print(f"Size: {file_data.get_dict_data().get('size')} bytes")
                    print(f"Properties: {file_data.get_dict_data().get('properties')}")
                    for property_name, property_value in file_data.get_dict_data().get('properties').items():
                        print(f"{property_name}: {property_value}")
                    print()