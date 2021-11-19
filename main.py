# import module

from random import randint
from colorama import Fore

# Config the main.py
numberofchords = 3                      # The number of suite of chords which you have


def main() :
    # Variable
    one = ["Em","Cm#","Fm#"]            # Define the all first chords which have in the suite of chords
    two = ["C", "G#", "Em"]             # Define the all second chords which have in the suite of chords
    three = ["G", "Fm#", "Bm"]          # Define the all third chords which have in the suite of chords
    four = ["D", "Cm#", "Am"]           # Define the all fourth chords which have in the suite of chords
    value = randint(0, numberofchords - 1)  # Define a variable value who is between 0 and numberofchords

    print(f"{Fore.BLUE}{one[value]} {two[value]} {three[value]} {four[value]}{Fore.WHITE}")

main()
