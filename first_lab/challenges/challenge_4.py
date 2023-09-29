class MemberSystem:
    """A class that represents a member of a golf club."""

    def __init__(self, name, age, handicap):
        """Initialize a member with a name, age and handicap."""
        self.name = name
        self.age = age
        self.handicap = handicap
        self.category = "UNDEFINED"

    def assign_category(self):
        """Assign a category to the member based on their age and handicap."""
        if self.age > 55 and self.handicap > 7:
            self.category = "SENIOR"
        else:
            self.category = "OPEN"

    def printCategory(self):
        """Print the category of the member."""
        print(self.category)


if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    handicap = int(input("Enter your handicap: "))

    member = MemberSystem(name, age, handicap)
    member.assign_category()
    member.printCategory()
