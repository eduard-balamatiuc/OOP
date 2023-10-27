class File:
    """This is a class that will represent a file in a file system."""
    def __init__(
        self,
        path,
        name,
        extension,
        size,
        created_at,
        updated_at,
        properties,
        ):
        """This is a constructor for the File class.

        Args:
            path (str): The path of the file.
            type (str): The type of the file.
            name (str): The name of the file.
            extension (str): The extension of the file.
            size (int): The size of the file.
            created_at (str): The date the file was created at.
            updated_at (str): The date the file was updated at.
            properties (dict): The properties of the file.
        """
        self.__path = path
        self.__name = name
        self.__extension = extension
        self.__size = size
        self.__created_at = created_at
        self.__updated_at = updated_at
        self.__properties = properties
        
    def get_path(self):
        """This is a getter for the path of the file.

        Returns:
            str: The path of the file.
        """
        return self.__path
    
    def get_name(self):
        """This is a getter for the name of the file.

        Returns:
            str: The name of the file.
        """
        return self.__name
    
    def get_extension(self):
        """This is a getter for the extension of the file.

        Returns:
            str: The extension of the file.
        """
        return self.__extension
    
    def get_size(self):
        """This is a getter for the size of the file.

        Returns:
            int: The size of the file.
        """
        return self.__size
    
    def get_created_at(self):
        """This is a getter for the date the file was created at.

        Returns:
            str: The date the file was created at.
        """
        return self.__created_at
    
    def get_updated_at(self):
        """This is a getter for the date the file was updated at.

        Returns:
            str: The date the file was updated at.
        """
        return self.__updated_at
    
    def get_properties(self):
        """This is a getter for the properties of the file.

        Returns:
            dict: The properties of the file.
        """
        return self.__properties
    
    def set_path(self, path):
        """This is a setter for the path of the file.

        Args:
            path (str): The path of the file.
        """
        self.__path = path
        
    def set_name(self, name):
        """This is a setter for the name of the file.

        Args:
            name (str): The name of the file.
        """
        self.__name = name
        
    def set_extension(self, extension):
        """This is a setter for the extension of the file.

        Args:
            extension (str): The extension of the file.
        """
        self.__extension = extension
        
    def set_size(self, size):
        """This is a setter for the size of the file.

        Args:
            size (int): The size of the file.
        """
        self.__size = size
        
    def set_created_at(self, created_at):
        """This is a setter for the date the file was created at.

        Args:
            created_at (str): The date the file was created at.
        """
        self.__created_at = created_at
        
    def set_updated_at(self, updated_at):
        """This is a setter for the date the file was updated at.

        Args:
            updated_at (str): The date the file was updated at.
        """
        self.__updated_at = updated_at
        
    def set_properties(self, properties):
        """This is a setter for the properties of the file.

        Args:
            properties (dict): The properties of the file.
        """
        self.__properties = properties
        
    def __str__(self):
        """This is a method that returns a string representation of the file.

        Returns:
            str: A string representation of the file.
        """
        return (
            f"File("
            f"path={self.__path}, "
            f"type={self.__type}, "
            f"name={self.__name}, "
            f"extension={self.__extension}, "
            f"size={self.__size}, "
            f"created_at={self.__created_at}, "
            f"updated_at={self.__updated_at}, "
            f"properties={self.__properties})"
        )
        
    