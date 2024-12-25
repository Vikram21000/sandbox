import pyfiglet
import random
import sys

def no_cmd():
    rand_num = random.randint(1, 549)
    fonts = pyfiglet.FigletFont.getFonts()[rand_num]
    figlet = pyfiglet.Figlet(font = fonts)
    reg_input = input("Input: ")
    words = figlet.renderText(reg_input)
    print("font =", fonts)
    print(words)

def yes_cmd():
    fonts = pyfiglet.FigletFont.getFonts()
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet = pyfiglet.Figlet(font = sys.argv[2])
            f_input = input("Input: ")
            print(figlet.renderText(f_input))

        else:
            sys.exit("Invalid usage")

    except pyfiglet.FontNotFound:
        sys.exit("Invalid usage")

if len(sys.argv) > 1:
    yes_cmd()
else:
    no_cmd()
