# Midnight Rider

import random
import sys
import textwrap
import time
import midnight_rider_text

# constants
MAX_FUEL = 50
MAX_CHIPS = 3
MAX_HUNGER = 50

ENDGAME_REASONS = {
    "LOSE_AGENTS": 1,
    "LOSE_FUEL": 2,
    "LOSE_HUNGER": 3
}

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
        hunger: describes how hungry our player is,
        represented by a number between 0-50,
        if hunger goes beyond 50, game is over.
        endgame_reason: shows the index of hte game ending
        text from midnight_rider_text.py
    """

    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_chips = MAX_CHIPS
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = 0

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
        agents_distance_now = random.randrange(10, 16)

        if user_choice == "a":
            if self.amount_chips > 0:
                self.amount_chips -= 1
                self.hunger = 0
                print(midnight_rider_text.EAT_TOFU)
            else:
                # Tell the player they don't have tofu
                print(midnight_rider_text.NO_TOFU)


        elif user_choice == "b":
        # Move the player slowly
            player_distance_now = random.randrange(5, 10)
            self.distance_traveled += player_distance_now
            self.agents_distance += agents_distance_now - player_distance_now
            self.fuel -= random.randrange(3, 8)
        # Give the player some feedback
            print(f"\n-------You drive conservatively.")
            print(f"-------You traveled {player_distance_now} kms.\n")

        elif user_choice == "c":
        # Move the player quickly
            player_distance_now = random.randrange(10, 16)
            self.distance_traveled += player_distance_now

        # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now

        # Burn fuel
            self.fuel -= random.randrange(5, 11)

        # Give the player some feedback
            print(f"\n-------ZOOOOOOOOOOM.")
            print(f"-------You traveled {player_distance_now} kms.\n")

        elif user_choice == "d":
            self.fuel = MAX_FUEL

            self.agents_distance += agents_distance_now

            print(midnight_rider_text.REFUEL)
            time.sleep(2)

        elif user_choice == "e":
            print("---Status Check---")
            print(f"Distance Traveled:{self.distance_traveled}kms")
            print(f"Fuel remaining: {self.fuel} L")
            print(f"Chips left {self.amount_chips}")
            print(f"Agent's Distance: {abs(self.agents_distance)} km behind")
            print("---")

        elif user_choice == "q":
            self.done = True
        time.sleep(2)

        if user_choice in ["b", "c", "d"]:
            self.hunger += random.randrange(8, 18)


    def upkeep(self) -> None:
        """Give the user reminder of hunger"""
        # TODO: update midnight_rider_text.py
        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)

        elif self.hunger > 25:
            print(midnight_rider_text.HUNGER)

    def check_endgame(self) -> None:
        """CHeck to see if win/lose conditions are met.
        If they're met, change the self.done flag."""
        if self.agents_distance >= 0:
            # Allows us to quite the while loop
            self.done = True
           # Helps with printing the right ending
            self.endgame_reason = ENDGAME_REASONS["LOSE_AGENTS"]

        if self.fuel <= 0:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_FUEL"]
        # TODO: Lose - Perish because of hunger
        if self.hunger > MAX_HUNGER:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_HUNGER"]
        # TODO: Win - Reach the goal


def main() -> None:
    game = Game()    # starting a new game
    # game.introduction()

    # Main loop
    while not game.done:
        game.upkeep()
        game.show_choices()
        game.get_choice()
        game.check_endgame()

    time.sleep(3)
    # print
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )



if __name__ == "__main__":
    main()
