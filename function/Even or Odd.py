def check_number():
    a=int(input("enter a number"))
    if a%2==0:
      return f"the number is even:{a}"
    else:
       return f"the number is odd: {a}"
result=check_number()
print(result) 
       