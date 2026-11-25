number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
opperator=input("Enter the opperator:")
if opperator not in "+-*/":
      print("invalid opperator")
else:      
 if opperator=='+':
      print(number1+number2)
 elif opperator=='-':
      print(number1-number2)
 elif opperator=='*':
      print(number1*number2)
 elif opperator=='/' and number2!=0:
      print(number1/number2)
 else:
      print("Mathematically undefined")



