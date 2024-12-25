def prompt():
    total_cost = 0
    total_cost = float(total_cost)
    while True:
        item = input("Item: ").title()
        total_cost = total_cost + menu[item]
        print("Amount due: " ,"$",format(total_cost,".2f"), sep = "")


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

try:
    prompt()

except (EOFError):
    print("")

except KeyError:
    prompt()
