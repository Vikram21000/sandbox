user=input("enter a maths problem: ")
x,y,z=user.split(" ")

x=float(x)
z=float(z)

if y=="+":
    print(x+z)
elif y=="-":
    print(x-z)
elif y=="*":
    print(x*z)
elif y=="/":
    print(x/z)
else:
    print("please use a valid operator (+,-,*,/)")

