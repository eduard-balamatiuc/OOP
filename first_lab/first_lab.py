class GameObject:
    def __init__(self, name, state="standing", speed=0, color="white"):
        self.name = name
        self.state = state
        self.speed = speed
        self.color = color

    def update_state(self, new_state):
        self.state = new_state

    def update_speed(self, new_speed):
        self.speed = new_speed

    def update_color(self, new_color):
        self.color = new_color

    def inform_user(self):
        print(f"{self.name} is {self.state} with a speed of {self.speed} and color {self.color}")


# Example usage:
if __name__ == "__main__":
    obj1 = GameObject("Object 1")
    obj1.inform_user()

    obj2 = GameObject("Object 2", "moving", 10, "red")
    obj2.inform_user()

    obj2.update_state("standing")
    obj2.inform_user()

    obj2.update_speed(0)
    obj2.inform_user()
