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
        student_info: str
    ):
        """_summary_

        Args:
            student_info (str): "    <student_first_name>, ",
                  "<student_last_name>, ",
                  "<student_email>, ",
                  "<student_enrollment_date>, ",
                  "<student_graduation_status>, ",
                  "<student_birth_date>"
        """
        pass
    
    def graduate_student(
        self, 
        student_id: int,
    ):
        pass
    
    def display_graduated_students(
        self,
    ):
        pass
    
    def check_student_information(
        self,
        student_id: int,
    ):
        pass
    
    def display_all_students(
        self,
    ):
        pass
    
    def add_faculty(
        self,
        faculty_info: str,
    ):
        """_summary_

        Args:
            faculty_info (str): "    <faculty_name>, ",
                  "<faculty_abbreviation>, ",
                  "<faculty_field>",
        """
        pass

    def display_all_faculties(
        self,
    ):
        pass
    
    def display_faculties_by_field(
        self,
        field: str,
    ):
        pass
    
    def search_faculty_by_student(
        self,
        student_id: int,
    ):
        pass
    
    def check_faculty_information(
        self,
        faculty_id: int,
    ):
        pass
    
    def update_faculty_name(
        self,
        faculty_id: int,
        faculty_name: str,
    ):
        pass
    
    def update_faculty_abbreviation(
        self,
        faculty_id: int,
        faculty_abbreviation: str,
    ):
        pass
    
    def update_faculty_field(
        self,
        faculty_id: int,
        faculty_field: str,
    ):
        pass
    
    def update_student_first_name(
        self,
        student_id: int,
        student_first_name: str,
    ):
        pass
    
    def update_student_last_name(
        self,
        student_id: int,
        student_last_name: str,
    ):
        pass
    
    def update_student_email(
        self,
        student_id: int,
        student_email: str,
    ):
        pass
    
    def update_student_enrollment_date(
        self,
        student_id: int,
        student_enrollment_date: str,
    ):
        pass
    
    def update_student_graduation_status(
        self,
        student_id: int,
        student_graduation_status: bool,
    ):
        pass
    
    def update_student_birth_date(
        self,
        student_id: int,
        student_birth_date: str,
    ):
        pass
    