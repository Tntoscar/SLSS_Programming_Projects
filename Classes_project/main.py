class vehicle:
    """ A class to represent a car

     It's name is Vehicle and it has the
     following attributes/methods:

    name: str
        what the name of the car is
    max_speed: int
          what the maximum speed the vehicle can go
    capacity: int
         how many people vehicle can hold
    Returns:
        None
    """
    def __init__(self, name: str, capacity: int, max_speed: int):
        """Creates a new vehicle with new default values"""
        self.name = vehicle
        self.max_speed = max_speed
        self.capacity = capacity


    def vroom(self) -> None:
        """prints vroom the number of times of max speed"""
        for i in range(self.max_speed):
            print("VROOMMMM!!!")
Toyota = vehicle("Toyota", 5, 10)
print(Toyota.max_speed)




