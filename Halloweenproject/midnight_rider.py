# Midnight Rider

import random
import sys
import textwrap
import time
import midnight_rider_text

# constants
MAX_FUEL = 50
MAX_CHIPS = 3

# A text - based game of intrigue and illusion

class Game:
    """Represent our game engine

    Attribute:
        done: describes if the game is
              finished or not -bool
        distance_traveled: describe the dsitance
            that we've traveled so far this game.
            in km
        amount_of_chips: how much chips we have
            left in our inventory
        agent_distance: describes
        the distance between the player and the agents
        fuel: describes the amount of fuel remaining ,
        starts off at 50
    """

    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_chips = MAX_CHIPS
        self.agents_distance = -20
        self.fuel = MAX_FUEL
    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect."""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    def show_choices(self) -> None:
        """show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)


    def get_choice(self) -> None:
        """Gets the user's choice and changes
        the environment"""
        # Get the user's response
        user_choice = input().strip("<>?!").lower()
        # Based on their choice, change the attribute
        # of their class
       # TODO: implement eaitng/hunger
        agents_distance_now = random.randrange(10, 16)
        if user_choice == "b":
            player_distance_now = random.randrange(1, 11)
            self.distance_traveled += player_distance_now
            # move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # burn the fuel
            self.fuel -= random.randrange(1, 10)
            # give the player feedback
            print(f"\n---------- You drive slow.")
            print(f"---------- You traveled {player_distance_now} kms.\n")


        elif user_choice == "c":
            #move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_traveled += player_distance_now
            #move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            #burn the fuel
            self.fuel -= random.randrange(5, 11)
            #give the player feedback
            print(f"\n----------ZOOOOOOOOM.")
            print(f"---------- You traveled {player_distance_now} kms.\n")

        elif user_choice == "d":
            self.fuel = MAX_FUEL
            self.agents_distance += random.randrange(7, 15)

            print(midnight_rider_text.REFUEL)
            time.sleep(2)
        elif user_choice == "e":
            print("---Status Check---")
            print(f"Distance Traveled:{self.distance_traveled}kms")
            print(f"Fuel remaining: {self.fuel} L")
            print(f"Chips left {self.amount_chips}")
            print(f"Agent's Distance: {abs(self.agents_distance)} km behind")
            print("---")
            time.sleep(2)
        elif user_choice == "q":
            self.done = True


def main() -> None:
    game = Game()    #starting a new game
    # game.introduction()

    # Main loop
    while not game.done:
           # Display the choices to the player
           game.show_choices()
           #  ask the player what they want to do
           # Change the state of  the environment
           game.get_choice()
           # TODO: Check win/lose conditions



if __name__ == "__main__":
    main()