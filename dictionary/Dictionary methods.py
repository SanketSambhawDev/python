
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

student.pop("age")
print(student)
