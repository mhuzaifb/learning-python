student = {
    "name":"Huzaif",
    "age":18,
    "course":"Biochemistry",
    "college":"SP College"
}
print("Student:", student)
print(type(student))
print(student["name"])
print(student.get("course"))
student["age"] = 19
student["minor"] = "Bioinformatics"
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, ':', value)