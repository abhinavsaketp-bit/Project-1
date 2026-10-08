def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

try:
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    operation=input("Enter an operation: ")

    if operation=="+":
        print("The addition of the two numbers is:", addition(num1,num2))
    elif operation=="-":
        print("The subtraction of the two numbers is:", subtraction(num1,num2))
    elif operation=="x" or operation=="*":
        print("The multiplication of the two numbers is:", multiplication(num1,num2))
    elif operation=="/":
        print("The division of the two numbers is:", division(num1,num2))
except ZeroDivisionError:
    print("You can not divide by zero!")
except ValueError:
    print("The input must only be a integer value!")
except:
    print("There is an error in your input!")

        
