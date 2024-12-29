import RPi.GPIO as GPIO
import string
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

def morse_translator():
    morse = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',

        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ' ': '/'
    }
    
    while True:
        user = input("Enter a phrase: ").upper()
        punc = string.punctuation
        
        if any(i in punc for i in user):
            print("try again.")
        else:
            for i in user:
                #print(morse[i], end="")
                morse_j = morse[i]
                for j in morse_j:
                    if j=="-":
                        #print("dash")
                        GPIO.output(17, GPIO.HIGH)
                        time.sleep(0.75)
                        GPIO.output(17, GPIO.LOW)
                        time.sleep(0.75)
                    elif j==".":
                        #print("dot")
                        GPIO.output(17, GPIO.HIGH)
                        time.sleep(0.25)
                        GPIO.output(17, GPIO.LOW)
                        time.sleep(0.75)
                    elif j=="/":
                        #print("slash")
                        GPIO.output(27, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(27, GPIO.LOW)
                        time.sleep(0.75)
                
                    

            #print("\n")

def main():
    while True:
        morse_translator()
        GPIO.cleanup()

main()
