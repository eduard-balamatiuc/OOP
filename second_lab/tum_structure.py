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
