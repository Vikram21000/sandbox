#s = input("vanity plate: ")
'''counter = 0

s = input("enter a plate: ")
for i in range(len(s) - 1):
    if s[i].isdigit():
        if s[i] == "0":
            print("invalid")
            counter += 1
            break
        if s[i+1].isalpha():
            print("invalid")
            counter += 1
            break
print(counter)'''
'''
s = "abc123"

for i in range(len(s) - 1):
    print(s[i+1])

'''
'''
s = input("vanity plate: ")
counter = 0
s_len = len(s)
sliced = s[1:s_len-1]
print(sliced)

    if first == "0":
        print("invalid")

    if sliced.isalpha() == True:
        print("valid")
        counter = counter + 1

    elif sliced.isalpha() == False:
        print("invalid")



'''
'''if s.isalpha():
    counter += 1
    print("valid 3")
else:
    print("invalid 3: no punctuation ")
'''

pwd = input("enter a pwd: ")

if pwd.isdecimal():
    print("is decimal")
else:
    print("not working")
