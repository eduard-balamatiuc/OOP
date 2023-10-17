class StudyField:
    """A class representing a field of study.

    Args:
        field (str): The initial field of study.

    Attributes:
        available_fields (list): A list of valid field names.

    Raises:
        ValueError: If the provided field is not in the list of available fields.
    """

    available_fields = [
        "MECHANICAL_ENGINEERING",
        "SOFTWARE_ENGINEERING",
        "FOOD_TECHNOLOGY",
        "URBANISM_ARCHITECTURE",
        "VETERINARY_MEDICINE",
    ]

    def __init__(
        self,
        field,
    ):
        """Initialize a new StudyField instance."""
        self.set_field(field)

    def set_field(
        self,
        field,
    ):
        """Set the field of study.

        Args:
            field (str): The field of study to set.

        Raises:
            ValueError: If the provided field is not in the list of available fields.
        """
        if field in self.available_fields:
            self.field = field
        else:
            raise ValueError(f"'{field}' is not a valid field of study")

    def __str__(
        self,
    ):
        """Return a string representation of the field of study."""
        return self.field
