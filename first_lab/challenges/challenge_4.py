class MemberSystem:
    def __init__(self, name, age, handicap):
        self.name = name
        self.age = age
        self.handicap = handicap
        self.category = "UNDEFINED"

    def assign_category(self):
        if (self.age>55 and self.handicap>7):
            self.category = "SENIOR"
        else:
            self.category = "OPEN"

    def printCategory(self):
        print(self.category)


if __name__=="__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    handicap = int(input("Enter your handicap: "))

    member = MemberSystem(name, age, handicap)
    member.assign_category()
    member.printCategory()
    