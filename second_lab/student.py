from datetime import date, datetime

class Student:
    """A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        email (str): The email address of the student.
        enrollment_date (str): The date when the student was enrolled.
        birth_date (str): The date of birth of the student.
    """

    def __init__(
        self,
        first_name: str = "undefined",
        last_name: str = "undefined",
        email: str = "undefined",
        enrollment_date: date = date.today(),
        graduation_status: str = "0",
        birth_date: date = None,
        student_dict_data: dict = None,
    ):
        """Initialize a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            email (str): The email address of the student.
            enrollment_date (date): The date when the student was enrolled.
            graduation_status (bool): The graduation status of the student.
            birth_date (date): The date of birth of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.graduation_status = bool(int(graduation_status))
        self.birth_date = birth_date
        if student_dict_data:
            self.load_student(student_dict_data)

    def __str__(
        self,
    ) -> str:
        return (
        f"{self.first_name} {self.last_name} ({self.email}) "
        f"born on {self.birth_date} and was "
        f"enrolled on {self.enrollment_date} and he/she did "
        f"{'graduate' if self.graduation_status else 'not graduate'}"
    )
        
    def change_attribute(
        self,
        attribute_name,
        new_value,
    ):
        """Change a student's attribute to a new value.

        Args:
            attribute_name (str): The name of the attribute to be changed.
            new_value: The new value to set for the attribute.

        Raises:
            AttributeError: If the attribute does not exist.
        """
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, new_value)
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attribute_name}'")

    def to_dict(
        self,
    ) -> dict:
        """Returns the student as a dictionary.

        Returns:
            dict: The student as a dictionary.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "enrollment_date": self.enrollment_date, 
            "graduation_status": self.graduation_status,
            "birth_date": self.birth_date,
        }
        
    def load_student(
        self,
        student_dict_data: dict,
    ) -> None:
        """Loads student data from the given dictionary.

        Args:
            student_dict_data (dict): The dictionary to load student data from.
        """
        self.first_name = student_dict_data["first_name"]
        self.last_name = student_dict_data["last_name"]
        self.email = student_dict_data["email"]
        self.enrollment_date = datetime.strptime(student_dict_data["enrollment_date"], "%d.%m.%Y").date()
        self.graduation_status = student_dict_data["graduation_status"]
        self.birth_date = datetime.strptime(student_dict_data["birth_date"], "%d.%m.%Y").date()