class GameObject:
    """A class representing a game object."""

    def __init__(self, name, state="standing", speed=0, color="white"):
        """Initialize a game object with a name, state, speed, and color."""
        self.name = name
        self.state = state
        self.speed = speed
        self.color = color

    def update_state(self, new_state):
        """Update the state of the game object."""
        self.state = new_state

    def update_speed(self, new_speed):
        """Update the speed of the game object."""
        self.speed = new_speed

    def update_color(self, new_color):
        """Update the color of the game object."""
        self.color = new_color

    def inform_user(self):
        """Print the state of the game object."""
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
