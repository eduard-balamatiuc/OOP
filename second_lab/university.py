from faculty import Faculty
from student import Student


class University:
    """A class representing a university.

    Attributes:
        faculties (list[Faculty]): A list of faculties in the university.
    """

    def __init__(
        self,
    ):
        """
        Initializes a new instance of the University class.
        """
        self.faculties = []
    
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

    def find_faculty_by_student(
        self,
        student: Student,
    ) -> Faculty:
        """Finds the faculty that the given student belongs to.

        Args:
            student (Student): The student to search for.
            
        Returns:
            Faculty: The faculty that the given student belongs to.
        """
        for faculty in self.faculties:
            if faculty.has_student(student):
                return faculty
        return None

    def get_faculties_by_field(
        self,
        field: str,
    ) -> list:
        """Returns a list of faculties that belong to the given study field.

        Args:
            field (str): The study field to search for.

        Returns:
            List[Faculty]: A list of faculties that belong to the given study field.
        """
        return [faculty for faculty in self.faculties if faculty.study_field == field]

    def display_all_faculties(
        self,
    ) -> None:
        """Displays information about all the faculties in the university."""
        for faculty in self.faculties:
            print(f"Faculty: {faculty.name} ({faculty.abbreviation}), Field: {faculty.study_field}")

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