import random


def main():
    ...


def get_level():
    try:
        level = int(input("Level: "))
        if 0 < level < 4:
            return level
    except ValueError:
        pass

def generate_integer(level):

    if level == 1:
        x = random.randint(1,9)
        y = random.randint(1,9)

        print(f"{x} + {y} = {answer}", end = "")
        answer = int(input())

    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)


if __name__ == "__main__":
    main()
