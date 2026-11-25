number=123

reverse=0
while number!=0:
    number1 = number%10
    reverse=reverse*10+number1
    number=number//10
print(reverse)
