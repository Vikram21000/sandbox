type=input("File name: ")
lowtype=type.lower().strip()
ending=lowtype.endswith(" ")

ending1=lowtype.endswith(".gif")
ending2=lowtype.endswith(".jpg")
ending3=lowtype.endswith(".jpeg")
ending4=lowtype.endswith(".png")
ending5=lowtype.endswith(".pdf")
ending6=lowtype.endswith(".txt")
ending7=lowtype.endswith(".zip")

if ending1==True:
    print("image/gif")
elif ending2==True:
    print("image/jpeg")
elif ending3==True:
    print("image/jpeg")
elif ending4==True:
    print("image/png")
elif ending5==True:
    print("application/pdf")
elif ending6==True:
    print("text/plain")
elif ending7==True:
    print("application/zip")
else:
    print("application/octet-stream")