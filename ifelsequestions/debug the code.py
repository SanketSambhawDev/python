age = int(input("Enter your age: "))
has_id = input("Do you have ID? ")
if age<18 or has_id=="no":
    print("you are not eligible")
elif age >= 18 and has_id == "yes":
    print("You are eligible")
else:
    print("You are not eligible")