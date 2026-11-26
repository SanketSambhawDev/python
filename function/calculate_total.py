def calculate_total(**prices):
    a=0
    for key, value in prices.items():
        a+=value
    return a
total= calculate_total(rice=20,wheet=40,pilse=56)
print(total)    
              