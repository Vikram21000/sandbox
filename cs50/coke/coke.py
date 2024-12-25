cokeprice = 50
print("Amount Due:", cokeprice)


while cokeprice > 0:
   insertcoins = int(input("Insert Coin: "))
   if insertcoins == 25 or  insertcoins == 10 or insertcoins == 5:
      cokeprice = cokeprice - insertcoins

      if cokeprice <= 0:
         print("Change Owed:", cokeprice*-1)
      else:
         print("Amount Due:", cokeprice)

   else:
      print("Amount Due:", cokeprice)
   #insertcoins = int(input("Insert Coin: "))
