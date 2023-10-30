import struct
import imghdr

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
        properties = {},
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
        if not properties:
            self.extract_properties()
        else:
            self.__properties = properties
        
    # create a function that will return a dict with the file data when calling the object  
    def get_dict_data(self):
        """This is a method that will return a dict with the file data when calling the object."""
        return {
            "path": self.__path,
            "name": self.__name,
            "extension": self.__extension,
            "size": self.__size,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "properties": self.__properties,
        }
    
    def extract_properties(self):
        """This is a method that will extract the properties of the file."""
        pass
    
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

class ImageFile(File):
    def __init__(self, path, name, extension, size, created_at, updated_at):
        super().__init__(path, name, extension, size, created_at, updated_at)

    def extract_properties(self):
        with open(self.get_path(), "rb") as image:
            head = image.read(24)
            if len(head) != 24:
                return
            if imghdr.what(self.get_path()) == "png":
                width, height = struct.unpack(">ii", head[16:24])
            elif imghdr.what(self.get_path()) == "gif":
                width, height = struct.unpack("<HH", head[6:10])
            elif imghdr.what(self.get_path()) == "jpeg":
                try:
                    image.seek(0)
                    size = 2
                    ftype = 0
                    while not 0xc0 <= ftype <= 0xcf:
                        image.seek(size, 1)
                        byte = image.read(1)
                        while ord(byte) == 0xff:
                            byte = image.read(1)
                        ftype = ord(byte)
                        size = struct.unpack(">H", image.read(2))[0] - 2
                    image.seek(1, 1)
                    height, width = struct.unpack(">HH", image.read(4))
                except Exception:
                    return
            else:
                return
            self.set_properties({
                "width": width,
                "height": height,
            })

class CodeFile(File):
    def __init__(self, path, name, extension, size, created_at, updated_at):
        super().__init__(path, name, extension, size, created_at, updated_at)

    def extract_properties(self):
        with open(self.get_path(), "r") as code:
            code_content = code.read()
            line_count = len(code_content.split("\n"))
            class_count = len(code_content.split("class")) - 1
            method_count = len(code_content.split("def")) - 1
            self.set_properties({
                "line_count": line_count,
                "class_count": class_count,
                "method_count": method_count,
            })

class TextFile(File):
    def __init__(self, path, name, extension, size, created_at, updated_at):
        super().__init__(path, name, extension, size, created_at, updated_at)


    def extract_properties(self):
        with open(self.get_path(), "r") as file:
            file_content = file.read()
            line_count = len(file_content.split("\n"))
            word_count = sum([len(line.split(" ")) for line in file_content.split("\n")])
            character_count = sum([len(line) for line in file_content.split("\n")])
            self.set_properties({
                "line_count": line_count,
                "word_count": word_count,
                "character_count": character_count,
            })
            