balance=1000


def deposite():
 ammount=int(input("enter your amount"))
 while ammount!=0:
  global balance
  balance=balance +ammount
  ammount=int(input("enter another ammount"))
  print("updated_balance",balance)
deposite()  
