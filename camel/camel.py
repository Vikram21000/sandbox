camelcase=input("enter a phrase: ")

for i in camelcase:
    if i.islower():
        print(i, end="")
    if i.isupper():
        i=i.lower()
        print("_",i, end="", sep="")
print("")
