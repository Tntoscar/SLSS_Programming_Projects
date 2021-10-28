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
        self.name = ""
        self.max_speed = 0
        self.capacity = 0


    def vroom(self) -> None:
        """prints vroom the number of times of max speed"""
        print("vroom" * self.max_speed)

class Bus(vehicle):
    """Bus is a Vehicle that can drive
    humans around in it"""
    def fare(self, age: int) -> None:
            """Tells how much fare is for a particular age"""
            if 18 <= age <= 60:
                print("The fare of this bus ride is $5.00")
            else:
                print("You ride free! You are lucky")


a_vehicle = vehicle("Toyota", 372, 2)
a_vehicle.vroom()

a_bus = Bus("Tranklink Bus - 407", 35, 140)
a_bus.name = "Tranlink Bus - 407"

a_bus.fare(10)
a_bus.fare(10)
print()
a_bus.fare(-1)
a_bus.fare(0)
a_bus.fare(17)
a_bus.fare(18)
a_bus.fare(60)
a_bus.fare(61)





