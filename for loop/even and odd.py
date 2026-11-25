even=0
odd=0
n=int(input("enter your number:"))
for n in range(1,n+1):
    if n%2==0:
        even+=1
    else:
        odd+=1
print("total even number:",even)

print("total odd number:",odd)    
        