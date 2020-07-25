import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = [
    "John Lennon",
    "Paul McCartney",
    "George Harrison",
    "Ringo Starr"
]

def roll_dice(num_of_sides):
    return random.randint(1, num_of_sides)