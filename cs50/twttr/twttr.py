user_input=input("enter a phrase: ")

for i in user_input:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        print("", end="", sep="")
    else:
        print(i, end="", sep="")

print()
