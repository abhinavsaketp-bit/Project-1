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
    operation=input("Enter the operation: ").strip().capitalize()
    
    if operation=="Add":
        print(f"The addition of {num1} and {num2}:", addition(num1,num2))
    elif operation=="Subtract":
        print(f"The subtraction of {num1} and {num2}:", subtraction(num1,num2))
    elif operation=="Multiply":
        print(f"The multiplication of {num1} and {num2}:", multiplication(num1,num2))
    elif operation=="Divide":
        print(f"THe division of {num1} and {num2}:", division(num1,num2))
    else:
        print("Unknown operation")
except ValueError:
    print("Enter in numbers only")
except ZeroDivisionError:
    print("You can not divide by 0")
except:
    print("Unknown error")

finally:
    print("Thank you for using Abhinav's coded calculator!(ACC)")