name=input("what is your name")
height=float(input("what is your height"))
weapons=int(input("how many weapons do you have?"))
is_active=bool(input("enter true is yes or enter false if no"))
print(f"the entered name is{name}and the datatype is{type(name)} ")
print(f"my height is{height}and the datatype is{type(height)}")
print(weapons,type(weapons) )
print(is_active,type(is_active))

marks=8.96
a=int(marks)
print(f"the value of a is{a} and the datatype is {type(a)}")
age="12"
b=int(age)
print(f"the value of b is{b} and the datatype is {type(b)}") 
name="abhinav"
print(name[4])
print(name[0])
print(name[2])
print(name[-1])
print(name[0:4])