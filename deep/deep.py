#question
big_q=input("What is the answer to the answer to the Great Question of Life, the Universe and Everything? ")
low_q= big_q.lower().strip()

#logic
if low_q==str(42) or low_q=="forty-two" or low_q=="forty two":
    print("yes")
else:
    print("no")