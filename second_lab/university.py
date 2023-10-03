from faculty import Faculty


class University:
    def __init__(self):
        self.faculties = []

    def create_faculty(self, name, abbreviation, study_field):
        faculty = Faculty(name, abbreviation, study_field)
        self.faculties.append(faculty)
        return faculty

    def find_faculty_by_student(self, student):
        for faculty in self.faculties:
            if faculty.has_student(student):
                return faculty
        return None

    def get_faculties_by_field(self, field):
        return [faculty for faculty in self.faculties if faculty.study_field == field]

    def display_all_faculties(self):
        for faculty in self.faculties:
            print(f"Faculty: {faculty.name} ({faculty.abbreviation}), Field: {faculty.study_field}")