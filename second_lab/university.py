from faculty import Faculty
from student import Student


class University:
    """A class representing a university.

    Attributes:
        faculties (list[Faculty]): A list of faculties in the university.
    """

    def __init__(
        self,
        uni_dict_data: dict = None,
    ):
        """
        Initializes a new instance of the University class.
        """
        self.faculties = []
        if uni_dict_data:
            self.load_university(uni_dict_data)
    
    def __str__(
        self,
    ):
        """
        Returns a string representation of the University object.
        """
        return f"Technical University of Moldova with {len(self.faculties)} faculties"

    def create_faculty(
        self,
        name: str,
        abbreviation: str,
        study_field: str,
    ) -> Faculty:
        """Creates a new faculty with the given name, abbreviation and study field and adds it to the list of faculties.

        Args:
            name (str): The name of the faculty.
            abbreviation (str): The abbreviation or short name of the faculty.
            study_field (str): The field of study or specialization of the faculty.
            
        Returns:
            Faculty: The newly created faculty.
        """
        faculty = Faculty(name, abbreviation, study_field)
        self.faculties.append(faculty)
        return faculty

    def load_university(
        self,
        uni_dict_data: dict,
    ) -> None:
        """Loads university data from the given location.

        Args:
            location (str): The location to load university data from.
        """
        pass
    
    def to_dict(
        self,
    ) -> dict:
        """Returns the university as a dictionary.

        Returns:
            dict: The university as a dictionary.
        """
        return {
            "faculties": [faculty.to_dict() for faculty in self.faculties],
        }
        