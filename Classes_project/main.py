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
    def fare(selfself, age: int) -> None:
        """Tells how much the fare is for a partically person"""
        if age <= 0 and <= 17:
            print("You ride free")
        elif age < 61:
            print("The fare of this bus is $5.00")
        else:
            print(" You ride free")


a_vehicle = vehicle()
a_vehicle = "Toyota"
a_vehicle.max_speed = 372
a_vehicle.capacity = 2
a_vehicle.vroom()

a_bus = Bus()
a_bus.name = "Tranlink Bus - 407"
a_bus.capacity = 35
a_bus.max_speed = 140

a_bus.fare(10)






