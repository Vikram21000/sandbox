# Program to generate a random number from 1-6 and display on a 7 segment display
# Cleaned up the number generation and pin assignment
import random
#import RPi.GPIO as GPIO

#generate random number
rand_num = str(random.randint(1,6))
#map number to 7-s display segments
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
#print(rand_num, bitcode)

#Rpi GPIO pins used
pins = ["17", "27", "22", "5", "6", "13", "19"]

#Assign bits to GPIO pins
for i in range(len(pins)):
    pin = pins[i]
    #print(pin)
    if bitcode[i] == "0":
        print("GPIO",pin,"LOW")
    else:
        print("GPIO",pin,"HIGH")
#print(range(len(pins)))