import random
import sys


def valid_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass


def valid_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass

def main():

    level = valid_level()
    answer = random.randint(1, level)
    while True:
        guess = valid_guess()
        if guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            sys.exit("Just right!")

main()

