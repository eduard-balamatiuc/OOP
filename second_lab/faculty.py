class Faculty:
    def __init__(self, name, abbreviation, students, study_field) -> None:
        self.name = name
        self.abbreviation = abbreviation
        self.students = students
        self.study_field = study_field
        
    def enroll_student(self, student):
        self.students.append(student)

    def graduate_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def has_student(self, student):
        return student in self.students