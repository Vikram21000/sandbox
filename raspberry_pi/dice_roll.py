import random
#import RPi.GPIO as GPIO


rand_num = str(random.randint(1,6))
bin_dict = {
    "0": "1111110",
    "1": "1100000",
    "2": "1101101",
    "3": "1111001",
    "4": "0110011",
    "5": "1011011",
    "6": "1011111",
    "7": "1110000",
    "8": "1111111",
    "9": "1110011",
}
bitcode = bin_dict[rand_num]
print(rand_num, bitcode)

if bitcode[0] == "1":
    print("GPIO17 HIGH")
else:
    print("GPIO17 LOW")

if bitcode[1] == "1":
    print("GPIO27 HIGH")
else:
    print("GPIO27 LOW")

if bitcode[2] == "1":
    print("GPIO22 HIGH")
else:
    print("GPIO22 LOW")

if bitcode[3] == "1":
    print("GPIO5 HIGH")
else:
    print("GPIO5 LOW")

if bitcode[4] == "1":
    print("GPIO6 HIGH")
else:
    print("GPIO6 LOW")

if bitcode[5] == "1":
    print("GPIO13 HIGH")
else:
    print("GPIO13 LOW")

if bitcode[6] == "1":
    print("GPIO19 HIGH")
else:
    print("GPIO19 LOW")