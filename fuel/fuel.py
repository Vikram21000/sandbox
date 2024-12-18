def main():
    fraction = input("enter fraction: ")
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)

    try:
        z = (x/y)*100
        if x>y:
            raise ValueError

        elif y==0:
            raise ZeroDivisionError

    except (ValueError, ZeroDivisionError):
        main()

    else:
        if z>=99:
            print("F")
        elif z<=1:
            print("E")
        else:
            print(round(z), end = "")
            print("%")
main()
