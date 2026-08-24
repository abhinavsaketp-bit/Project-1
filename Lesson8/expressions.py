x=int(input("Send a value for x: "))
y=int(input("Send a value for y: "))
v=int(input("Send a value for v: "))
w=int(input("Send a value for w: "))

z=(v+w)*y/x
print(f"The value of z is {z}")
name=input("What is your name? ")
age=int(input("What is your age? "))
if name=="Alex" or name=="John" and age>=2:
    print("welcome to your files")
else:
    print("Create an account to join.")