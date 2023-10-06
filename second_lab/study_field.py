class StudyField:
    def __init__(self, field):
        self.available_fields = [
            "MECHANICAL_ENGINEERING",
            "SOFTWARE_ENGINEERING",
            "FOOD_TECHNOLOGY",
            "URBANISM_ARCHITECTURE",
            "VETERINARY_MEDICINE",
        ]
        self.field = field
        
    def set_field(self, field):
        if field in self.available_fields:
            self.field = field
        else:
            raise ValueError(f"{field} is not a valid field of study")

    def __str__(self):
        return self.field