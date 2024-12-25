
greeting=input("give me a greeting: ")
lowgreet=greeting.lower().strip()

try:
    if  lowgreet[0]=="h" and lowgreet[1]=="e" and lowgreet[2]=="l" and lowgreet[3]=="l" and lowgreet[4]=="o":
        print("$0")

    elif lowgreet[0] == "h":
        print("$20")

    else:
        print("$100")
except IndexError:
    print("please enter a greeting with 5 or more letters.")
