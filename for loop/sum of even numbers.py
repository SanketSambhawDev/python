n=int(input("enter your number:"))
u=0
for n in range(1,n+1):
    if n%2==0:
        u=u+n
print("the sum:",u)    