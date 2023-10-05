class Faculty:
    """Represents a faculty within a university.

    Attributes:
        name (str): The name of the faculty.
        abbreviation (str): The abbreviation or short name of the faculty.
        students (list): A list of students enrolled in the faculty.
        study_field (str): The field of study or specialization of the faculty.
    """

    def __init__(self, name, abbreviation, students, study_field, graduate_students):
        """Initializes a new Faculty instance.

        Args:
            name (str): The name of the faculty.
            abbreviation (str): The abbreviation or short name of the faculty.
            students (list): A list of students initially enrolled in the faculty.
            study_field (str): The field of study or specialization of the faculty.
        """
        self.name = name
        self.abbreviation = abbreviation
        self.students = students
        self.study_field = study_field
        self.graduate_students = graduate_students

    def enroll_student(self, student):
        """Enrolls a student in the faculty.

        Args:
            student: The student to be enrolled.
        """
        self.students.append(student)

    def graduate_student(self, student):
        """Graduates a student from the faculty.

        Args:
            student: The student to be graduated.
        """
        if student in self.students:
            self.graduate_students.append(student)
            self.students.remove(student)

    def has_student(self, student):
        """Checks if the faculty has a particular student.

        Args:
            student: The student to check for.

        Returns:
            bool: True if the student is enrolled in the faculty, False otherwise.
        """
        return student in self.students
