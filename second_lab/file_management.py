import os
import json


class File_management_system:
    """
    A class representing the file management system for TUM student structures.

    Methods:
        get_available_files(): Gets all the available files in the memory folder.
        get_structure_file(file_name: str): Gets the file with the given name.
        save_structure_file(file_name: str, file_content: dict): Saves the given file with the given name.
        delete_structure_file(file_name: str): Deletes the file with the given name.
        rename_structure_file(old_file_name: str, new_file_name: str): Renames the file with the given name to the new given name.
    """

    def get_available_files():
        """
        Gets all the available files in the memory folder.

        Returns:
            list: A list of all the available files in the memory folder.
        """
        # Check if there is a memory folder and get all the names of the JSON files without the extension
        files = []
        if os.path.isdir("memory"):
            files = os.listdir("memory")
            files = [file.split(".")[0] for file in files]
        else:
            os.mkdir("memory")
        return files

    def get_structure_file(
        file_name: str,
    ):
        """
        Gets the file with the given name.

        Args:
            file_name (str): The name of the file to get.

        Raises:
            FileNotFoundError: If the file with the given name does not exist.

        Returns:
            dict: The file with the given name.
        """
        # Get the file with the given name
        if os.path.isfile(f"memory/{file_name}.json"):
            with open(f"memory/{file_name}.json", "r") as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"File {file_name} does not exist")

    def save_structure_file(
        file_name: str,
        file_content: dict,
    ):
        """
        Saves the given file with the given name.

        Args:
            file_name (str): The name of the file to save.
            file_content (dict): The content of the file to save.
        """
        if not os.path.isdir("memory"):
            os.mkdir("memory")
        with open(f"memory/{file_name}.json", "w") as file:
            json.dump(file_content, file)

    def delete_structure_file(
        file_name: str,
    ):
        """
        Deletes the file with the given name.

        Args:
            file_name (str): The name of the file to delete.
        """
        if os.path.isfile(f"memory/{file_name}.json"):
            os.remove(f"memory/{file_name}.json")
        else:
            raise FileNotFoundError(f"File {file_name} does not exist")

    def rename_structure_file(
        old_file_name: str,
        new_file_name: str,
    ):
        """
        Renames the file with the given name to the new given name.

        Args:
            old_file_name (str): The name of the file to rename.
            new_file_name (str): The new name of the file.
        """
        if os.path.isfile(f"memory/{old_file_name}.json"):
            os.rename(f"memory/{old_file_name}.json", f"memory/{new_file_name}.json")
        else:
            raise FileNotFoundError(f"File {old_file_name} does not exist")
