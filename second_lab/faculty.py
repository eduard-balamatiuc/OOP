from student import Student
from study_field import StudyField
 

class Faculty:
    """Represents a faculty within a university.

    Attributes:
        name (str): The name of the faculty.
        abbreviation (str): The abbreviation or short name of the faculty.
        students (list[Student]): A list of students enrolled in the faculty.
        study_field (str): The field of study or specialization of the faculty.
        graduate_students (list[Student]): A list of students who have graduated from the faculty.
    """

    def __init__(
        self,
        name: str = "undefined",
        abbreviation: str = "undefined",
        study_field: StudyField = None,
        faculty_dict_data: dict = None,
    ):
        """Initializes a new Faculty instance.

        Args:
            name (str): The name of the faculty.
            abbreviation (str): The abbreviation or short name of the faculty.
            study_field (str): The field of study or specialization of the faculty.
        """
        self.name = name
        self.abbreviation = abbreviation
        self.study_field = study_field
        self.students = []
        self.graduate_students = []
        if faculty_dict_data:
            self.load_faculty(faculty_dict_data)

    def __str__(
        self,
    ) -> str:
        """Returns a string representation of the faculty.
        
        Returns:
            str: A string representation of the faculty.
        """
        return (
            f"{self.name} ({self.abbreviation}) with {len(self.students)} students "
            f"and {len(self.graduate_students)} graduates, "
            f"specializing in {self.study_field}"
        )

    def enroll_student(
        self,
        first_name: str = "undefined",
        last_name: str = "undefined",
        email: str = "undefined",
        enrollment_date: str = "undefined",
        graduation_status: bool = False,
        birth_date: str = "undefined",
    ):
        """Enrolls a student in the faculty.

        Args:
            student (Student): The student to be enrolled.
        """
        student = Student(
            first_name,
            last_name,
            email,
            enrollment_date,
            graduation_status,
            birth_date,
        )
        if student not in self.students:
            self.students.append(student)
        else:
            raise ValueError(f"{student} is already enrolled in the faculty")

    def graduate_student(
        self,
        student: Student,
    ):
        """Graduates a student from the faculty.

        Args:
            student (Student): The student to be graduated.
        """
        if student in self.students:
            student.graduation_status = True
            self.graduate_students.append(student)
            self.students.remove(student)
        else:
            raise ValueError(f"{student} is not enrolled in the faculty")

    def has_student(
        self,
        student: Student,
    ):
        """Checks if the faculty has a particular student.

        Args:
            student (Student): The student to check for.

        Returns:
            bool: True if the student is enrolled in the faculty, False otherwise.
        """
        return student in self.students

    def to_dict(
        self,
    ) -> dict:
        """Returns a dictionary representation of the faculty.

        Returns:
            dict: A dictionary representation of the faculty.
        """
        return {
            "name": self.name,
            "abbreviation": self.abbreviation,
            "study_field": self.study_field,
            "students": [student.to_dict() for student in self.students],
            "graduate_students": [student.to_dict() for student in self.graduate_students],
        }
        
    def load_faculty(
        self,
        faculty_dict_data: dict,
    ) -> None:
        """Loads faculty data from the given dictionary.

        Args:
            faculty_dict_data (dict): The dictionary to load faculty data from.
        """
        self.name = faculty_dict_data["name"]
        self.abbreviation = faculty_dict_data["abbreviation"]
        self.study_field = faculty_dict_data["study_field"]
        self.students = [Student(student_dict_data) for student_dict_data in faculty_dict_data["students"]]
        self.graduate_students = [
            Student(student_dict_data) for student_dict_data in faculty_dict_data["graduate_students"]
        ]