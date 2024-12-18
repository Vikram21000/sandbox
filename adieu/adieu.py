import inflect
p = inflect.engine()
name_list = []
try:
    while True:
        name = input("Name: ")
        name_list.append(name)
except EOFError:
    adieu = p.join(name_list)
    print("\n")
    print(f"Adieu, adieu, to {adieu}")
