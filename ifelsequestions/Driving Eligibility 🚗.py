age= int(input("enter your age:"))
if age<18:
    print("you are not eligible")
else: 
   has_licence= input("do you have a valid driving licence.")
   if has_licence=="yes":
     print("You can drive")
   elif has_licence=="no":
     print("you need a driving licence")
   else:
     print("Invalid response")               
