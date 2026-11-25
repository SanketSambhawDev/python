a=[75, 90, 60, 85, 70]
a[0]=80
a.append(95)
a.pop(2)
b=a.copy()
b.reverse()
print(a.sort(reverse=True))
print(a)
print(b)
print(len(a))
print(90 in a)