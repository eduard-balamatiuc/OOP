class User:
    """A class that represents a user with first and last name."""

    def __init__(self, firstName, lastName):
        """Initialize a user with a first and last name."""
        self.firstName = firstName
        self.lastName = lastName

    def convert_name(self):
        """Convert the user's first and last name to initials."""
        print(f"{self.firstName[0]}.{self.lastName[0]}")


if __name__ == "__main__":
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")

    user = User(firstName, lastName)
    user.convert_name()
