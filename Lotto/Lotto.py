##import secrets
import random
import sys

LOTTO = list(range(1,37))

def get_result(numbers):
    """Draws and checks if 6 given numbers are same as drawn numbers from LOTTO list

    Args:
        numbers (list): list of unique numbers

    Returns:
        str: how many numbers we bet correctly
    """
    draw = random.sample(LOTTO, 6)
##    draw = secrets.SystemRandom().sample(LOTTO, 6) # secrets lib is another random method
    draw.sort()
    print("Drawn numbers: ", draw)
    result = len([True for i in draw if i in numbers])
    return f"You bet correctly {result} number(s)!"

def run():
    """Asks an user to enter 6 numbers"""
    numbers = []
    while len(numbers) != 6:
        try:
            number = int(input(f'Enter {len(numbers)+1} number: '))
        except ValueError:
            print(f"You may enter numbers from {LOTTO[0]} to {LOTTO[-1]} only!")
            continue
        if number > LOTTO[-1] or number < LOTTO[0]:
            print(f"Number must be between {LOTTO[0]} and {LOTTO[-1]}!")
        else:
            if number in numbers:
                print("You have already entered this number. Try another one.")
            else:
                numbers.append(number)
    numbers.sort()
    print("Your numbers: ", numbers)
    print(get_result(numbers))
    again = input("Do you want to try again? (y/n) ")
    if again.lower() == "y" or again.lower() == "yes":
        run()
    else:
        sys.exit(0)

if __name__ == "__main__":
    run()
