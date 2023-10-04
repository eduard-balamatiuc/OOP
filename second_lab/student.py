class Student:
    """A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        email (str): The email address of the student.
        enrollment_date (str): The date when the student was enrolled.
        birth_date (str): The date of birth of the student.
    """

    def __init__(self, first_name, last_name, email, enrollment_date, graduation_status, birth_date):
        """Initialize a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            email (str): The email address of the student.
            enrollment_date (str): The date when the student was enrolled.
            birth_date (str): The date of birth of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.graduation_status = graduation_status
        self.birth_date = birth_date

    def change_attribute(self, attribute_name, new_value):
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
