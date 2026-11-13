class student:
    grade=9
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=student("Abhinav",13)
student2=student("Romeo",14)

print("Student1 grade:", student1.grade)
print("Student2 grade:", student2.grade)

print("{} is {} years old.".format(student1.name,student1.age))
print("{} is {} years old.".format(student2.name,student2.age))

    