import json


class Tum_structure:
    def __init__(self) -> None:
        self.main_structure = {}
        self.structure_version = None

    def get_structure(self):
        return self.main_structure
    
    def set_structure(self, structure):
        self.main_structure = structure

    def get_structure_location(self):
        return self.structure_location
    
    def read_structure(self):
        with open(self.structure_location, "r") as file:
            self.main_structure = json.load(file)
