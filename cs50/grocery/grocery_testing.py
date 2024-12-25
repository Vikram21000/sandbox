grocery_list = {}
print("enter your grocery list: ")
while True:
    try:
        grocery = input().upper()
        if grocery:
            if grocery in grocery_list:
                grocery_list[grocery] += 1

            else:
                grocery_list[grocery] = 1
    except EOFError:
        break
for k,v in sorted(grocery_list.items()):
    print(v,k)
