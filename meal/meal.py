def  convert(time):

    hours,mins=time.split(":")

    hours=int(hours)
    mins=int(mins)

    minutes=(hours*60)+mins
  #  print("There are",minutes,"minutes in", hours,"hours and",mins,"minutes" )
    decimaltime=minutes/60
    roundtime=round(decimaltime,2)
  #  print(roundtime)
    return roundtime


def main():
    time = input("What is the time? ")
    value = convert(time)
    #print("main() ",value)

    if 7<=value<=8:
        print("breakfast time")

    elif 12<=value<=13:
        print("lunch time")

    elif 18<=value<=19:
        print("dinner time")

if __name__ == "__main__":
    main()
