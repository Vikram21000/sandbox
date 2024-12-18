def main():
    user=input("enter a sentence: ")
    converteduser=convert(user)
    print(converteduser)
def convert(string):
    string=string.replace(":)","🙂")
    string=string.replace(":(","🙁")
    return string
main()
