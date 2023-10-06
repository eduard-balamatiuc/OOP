from university import University
from file_management import File_management_system as fms


class Tum_structure:
    def __init__(
        self,
        selected_file,
    ) -> None:
        self.selected_file = selected_file
        self.university = University(fms.get_structure_file(self.selected_file))
