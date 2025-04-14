import array
'''
doorsensor = False
windowsensor = False
systemarmed = False

while systemarmed:
    if doorsensor or windowsensor:
        print("Sound the alarm!")
        break
    else:
        print("nothing to see here!")
        break
if not systemarmed:
    print("System unarmed")
'''
events = [["05/02/2023", "WS2", "Window", 38], ["06/02/2023", "MS1", "Motion", 2], ["07/02/2023", "DS3", "Door", 1]]
user_input = input("Enter a date in the form 'DD/MM/YYYY': ")

if user_input == events[0][0] or user_input == events[1][0] or user_input == events[2][0]:
    print(  )

for r in events:
    for c in r:
        print(c, end = " ")
    print()

