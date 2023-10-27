import os

class Fit:
    """A class structure that will mimic the git functionalities of git"""
    def __init__(self):
        pass
    
    def fit_check_hidden_system_folder(self):
        """This is a method that will check if the fit system was already initialized in the hidden folder."""
        folder_name = ".fit"
        folder_path = os.path.join(os.getcwd(), folder_name)
        
        if os.path.exists(folder_path):
            return True
        else:
            return False
        
    def fit_create_hidden_system(self):
        """This is a metho that will create the hidden folder for the fit system."""
        folder_name = ".fit"
        folder_path = os.path.join(os.getcwd(), folder_name)
        
        try:
            os.mkdir(folder_path)
        except OSError:
            print("Creation of the directory %s failed" % folder_path)
            return False
        
        # create the commit history json file in the hidden folder
        file_name = "commit_history.json"
        file_path = os.path.join(folder_path, file_name)
        
        try:
            open(file_path, 'w').close()
        except OSError:
            print("Creation of the file %s failed" % file_path)
            return False
        
        return True