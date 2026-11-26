def student_info(**info):
    for key, value in info.items():
        print(key,':',value)
student_info(name="sanket",age=23, course="Python",city="Kolkata")

student={"namee":"Sanket","age":23,"course":"Python","city":"Kolkata"}
for key, value in student.items():
    print(key,':',value) 
        

    