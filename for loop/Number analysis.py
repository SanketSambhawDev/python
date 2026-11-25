n=int(input("enter your number:"))
u=0
v=0
for  n in range(1,n+1):
    if n%3==0 and n%5==0:
        u+=1
    if n%3==0:
        v=v+n
print("the sum of the number divisible by 3:",v) 
print("Number divisible by both:",u)
