import os


class File_management_system:
    def __init__(self) -> None:
        pass

    def get_available_files(self):
        # check if athere is a memory folder and get all the namings all the json files without the extension
        files = []
        if os.path.isdir("memory"):
            files = os.listdir("memory")
            files = [file.split(".")[0] for file in files]
        else:
            os.mkdir("memory")
        return files