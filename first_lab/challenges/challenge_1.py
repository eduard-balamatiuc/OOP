class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def convert_name(self):
        print(f"{self.firstName[0]}.{self.lastName[0]}")


if __name__ == "__main__":
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")

    user = User(firstName, lastName)
    user.convert_name()
