import numpy as np
import secrets
import random

lotto = list(np.arange(1,37))

def get_result(numbers):
    draw = random.sample(lotto, 6)
    # x = secrets.SystemRandom().sample(lotto, 6) # secrets lib is another random method
    draw.sort()
    print("Drawn numbers: ", draw)
    result = 0
    for i in draw:
        if i in numbers:
            result += 1
    return print(f"You bet correctly {result} number(s)!") 

def run():
    i = 0
    numbers = []
    while i != 6:
        try:
            n1 = int(input(f'Enter {i+1} number: '))
        except ValueError:
            print("You may enter number from 1 to 36 only!")
            continue
        if n1 > 36 or n1 < 1:
            print("Number must be between 1 and 36!")
            continue
        else:
            if n1 in numbers:
                print("You have already entered this number. Try another one.")
            else:
                i += 1
                numbers.append(n1)
    numbers.sort()
    print("Your numbers: ", numbers)
    get_result(numbers)

if __name__ == "__main__":
    run()


