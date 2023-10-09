from university import University
from file_management import File_management_system as fms

class Tum_structure:
    def __init__(
        self,
        selected_file: str = None,
    ) -> None:
        self.selected_file = selected_file
        self.university = self.initialize_university()

    def initialize_university(self):
        if self.selected_file:
            return University(fms.get_structure_file(self.selected_file))
        else:
            return University()
        
    def add_student(
        self,
        student_info: str,
    ):
        """Add a new student to the university.

        Args:
            student_info (str): "    <student_first_name>, ",
                  "<student_last_name>, ",
                  "<student_email>, ",
                  "<student_enrollment_date>, ",
                  "<student_graduation_status>, ",
                  "<student_birth_date>"
        """
        self.university.create_student(*student_info.split(", "))
        print("Student added")
    
    def graduate_student(
        self, 
        student_id: int,
    ):
        """Graduate a student.
        
        Args:
            student_id (int): The ID of the student to graduate.
        """
        self.university.students[student_id].graduation_status = True
        print(f"Student {student_id} graduated")
        
    def display_enrolled_students(
        self,
    ):
        """Display all enrolled students."""
        for student in self.university.students:
            if not student.graduation_status:
                print(student)
    
    def display_graduated_students(
        self,
    ):
        """Display all graduated students."""
        for student in self.university.students:
            if student.graduation_status:
                print(student)
    
    def check_student_information(
        self,
        student_id: int,
    ):
        """Display information about a student.
        
        Args:
            student_id (int): The ID of the student to display information about.
        """
        print(self.university.students[student_id])
    
    def display_all_students(
        self,
    ):
        """Display information about all students in the university."""
        for faculty in self.university.faculties:
            for student in faculty.students:
                print(student)
    
    def add_faculty(
        self, 
        faculty_info: str,
    ):
        """Add a new faculty to the university.

        Args:
            faculty_info (str): A comma-separated string containing faculty information
                in the format: "<faculty_name>, <faculty_abbreviation>, <faculty_field>"
        """
        self.university.create_faculty(*faculty_info.split(", "))
        print("Faculty added")

    def display_all_faculties(
        self,
    ):
        """Display information about all faculties in the university."""
        for index, faculty in enumerate(self.university.faculties):
            print(f"Index: {index}, Faculty: {faculty.name} ({faculty.abbreviation}), Field: {faculty.study_field}")
            
    def display_faculties_by_field(
        self,
        field: str,
    ):
        """Display faculties within a specific field of study.

        Args:
            field (str): The field of study to filter faculties by.
        """
        matching_faculties = [faculty for faculty in self.university.faculties if faculty.study_field == field]

        if matching_faculties:
            for faculty in matching_faculties:
                print(f"Faculty: {faculty.name} ({faculty.abbreviation}), Field: {faculty.study_field}")
        else:
            print(f"No faculties found in the field: {field}")

    def search_faculty_by_student(
        self,
        student_id: int,
    ):
        """Search for a faculty by a student's ID.

        Args:
            student_id (int): The ID of the student to find within faculties.

        Returns:
            Faculty: The faculty associated with the student, or None if not found.
        """
        for faculty in self.university.faculties:
            if faculty.has_student(student_id):
                return faculty
        return None
    
    def check_faculty_information(
        self,
        faculty_id: int,
    ):
        """Display information about a faculty.
        
        Args:
            faculty_id (int): The ID of the faculty to display information about.
        """
        print(self.university.faculties[faculty_id])
    
    def update_faculty_name(
        self,
        faculty_id: int,
        faculty_name: str,
    ):
        """Update faculty name
        
        Args:
            faculty_id (int): The ID of the faculty to update.
            faculty_name (str): The new name of the faculty.
        """
        self.university.faculties[faculty_id].name = faculty_name
        print(f"Faculty {faculty_id} updated")
    
    def update_faculty_abbreviation(
        self,
        faculty_id: int,
        faculty_abbreviation: str,
    ):
        """Update faculty abbreviation
        
        Args:
            faculty_id (int): The ID of the faculty to update.
            faculty_abbreviation (str): The new abbreviation of the faculty.    
        """
        self.university.faculties[faculty_id].abbreviation = faculty_abbreviation
        print(f"Faculty {faculty_id} updated")
        
    def update_faculty_field(
        self,
        faculty_id: int,
        faculty_field: str,
    ):
        """Update faculty field
        
        Args: 
            faculty_id (int): The ID of the faculty to update.
            faculty_field (str): The new field of the faculty.
        """
        self.university.faculties[faculty_id].study_field = faculty_field
        print(f"Faculty {faculty_id} updated")
        
    def update_student_first_name(
        self,
        student_id: int,
        student_first_name: str,
    ):
        """Update student first name
        
        Args:
            student_id (int): The ID of the student to update.
            student_first_name (str): The new first name of the student.
        """
        self.university.students[student_id].first_name = student_first_name
        print(f"Student {student_id} updated")
    
    def update_student_last_name(
        self,
        student_id: int,
        student_last_name: str,
    ):
        """Update student last name
        
        Args:
            student_id (int): The ID of the student to update.
            student_last_name (str): The new last name of the student.
        """
        self.university.students[student_id].last_name = student_last_name
        print(f"Student {student_id} updated")
    
    def update_student_email(
        self,
        student_id: int,
        student_email: str,
    ):
        """Update student email
        
        Args:
            student_id (int): The ID of the student to update.
            student_email (str): The new email of the student.
        """
        self.university.students[student_id].email = student_email
        print(f"Student {student_id} updated")
    
    def update_student_enrollment_date(
        self,
        student_id: int,
        student_enrollment_date: str,
    ):
        """Update student enrollment date
        
        Args:
            student_id (int): The ID of the student to update.
            student_enrollment_date (str): The new enrollment date of the student.
        """
        self.university.students[student_id].enrollment_date = student_enrollment_date
        print(f"Student {student_id} updated")
    
    def update_student_graduation_status(
        self,
        student_id: int,
        student_graduation_status: bool,
    ):
        """Update student graduation status
        
        Args:
            student_id (int): The ID of the student to update.
            student_graduation_status (bool): The new graduation status of the student.
        """
        self.university.students[student_id].graduation_status = student_graduation_status
        print(f"Student {student_id} updated")
    
    def update_student_birth_date(
        self,
        student_id: int,
        student_birth_date: str,
    ):
        """Update student birth date
        
        Args:
            student_id (int): The ID of the student to update.
            student_birth_date (str): The new birth date of the student.
        """
        self.university.students[student_id].birth_date = student_birth_date
        print(f"Student {student_id} updated")
    