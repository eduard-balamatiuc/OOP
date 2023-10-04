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

    def get_field(self):
        return self.field

    def set_field(self, field):
        self.field = field

    def __str__(self):
        return self.field