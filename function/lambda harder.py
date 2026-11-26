largest=lambda a, b: "both are equals" if a==b else "a is largest" if a>b else"b is largest"
print(largest(
    int(input("Enter the first number: ")),
    int(input("Enter the second number: "))
))
