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
        """Initializes a new instance of the University class.

        Args:
            uni_dict_data (dict): The dictionary data of the university.
        """
        self.faculties = []
        self.students = []
        if uni_dict_data:
            self.load_university(uni_dict_data)

    def __str__(
        self,
    ):
        """Returns a string representation of the University object."""
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

    def create_student(
        self,
        faculty_id: str,
        first_name: str,
        last_name: str,
        email: str,
        enrollment_date: str,
        graduation_status: bool,
        birth_date: str,
    ) -> Student:
        """Creates a new student with the given first name, last name, email, enrollment date, graduation status and
        birth date and adds it to the list of students.

        Args:
            faculty_id (str): The ID of the faculty to add the student to.
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            email (str): The email address of the student.
            enrollment_date (str): The date when the student was enrolled.
            graduation_status (bool): The graduation status of the student.
            birth_date (str): The date of birth of the student.

        Returns:
            Student: The newly created student.
        """
        student = Student(first_name, last_name, email, enrollment_date, graduation_status, birth_date)
        self.students.append(student)
        self.faculties[int(faculty_id)].students.append(student)
        return student

    def load_university(
        self,
        uni_dict_data: dict,
    ) -> None:
        """Loads university data from the given location.

        Args:
            uni_dict_data (dict): The dictionary data of the university.
        """
        for faculty in uni_dict_data["faculties"]:
            self.faculties.append(Faculty(faculty_dict_data=faculty))

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
