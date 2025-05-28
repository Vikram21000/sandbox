import random

try:
    counter = 10
    level = int(input("Level: "))

    if level < 1 or level > 3:
        print("Somthing's up with level validation")
        raise ValueError

    if level == 1:
        for i in range(1,counter+1):
            x = random.randint(1,9)
            y = random.randint(1,9) 
            print(f"{x} + {y} = ")
            response = int(input())
            if response != (x+y):
                for i in range(1,4):
                    print(f"{x} + {y} = ")
                    response = int(input())
                    if response == (x+y):
                        continue
                    else:
                        continue
            counter += 1
    elif level == 2:
        for i in range(1,counter+1):
            x = random.randint(10,99)
            y = random.randint(10,99) 
            print(f"{x} + {y} = ")
            response = int(input())
            counter += 1
    elif level == 3:
        for i in range(1,counter+1):
            x = random.randint(100,999)
            y = random.randint(100,999) 
            print(f"{x} + {y} = ")
            response = int(input())
            counter += 1              
        

    else:
        print("Something's up with level generation")
        raise ValueError



except ValueError:
    print("Something went wrong :(")

