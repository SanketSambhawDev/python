a = 5
b = 0
c = 10
if a<=0 or b<=0 or c<=0:
    print("the triangle is invalid")
else:
    if a+b>c and b+c>a and a+c>b:
        print("the triangle is valid")
    else:
        print("the triangle is invalid")       