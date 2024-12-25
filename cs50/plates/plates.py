import string

def main(): # --------------------------------------------> main function
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s): # ----------------------------------------> is_valid function
    if length(s) and first_two(s) and mid_num(s) and not_alphanumeric(s):
        return True
    else:
        return False

def length(s): # ------------------------------------------> length
    plate_len = len(s)
    if 6>=plate_len >= 2:
        return True

def first_two(s): # ---------------------------------------> first two characters
    first = s[0]
    second = s[1]
    if first.isalpha() and second.isalpha():
        return True

def mid_num(s): # -----------------------------------------> middle numbers
    for i in range(len(s) - 1):
        if s[i].isdigit():
            if s[i] == "0":
                break
            if s[i+1].isalpha():
                break
            else:
                return True

def not_alphanumeric(s): # -------------------------------------> punctuation
    punctuation = string.punctuation
    if punctuation not in s:
        return True
    else:
        return False

main()
