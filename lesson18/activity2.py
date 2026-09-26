try:
    print("Enter 2 numbers seprated by a comma")
    num1,num2=eval(input("Enter the two number"))
    print("The division of the two number is", num1/num2)
except ZeroDivisionError:
    print("The denominator is 0 so it is a 0 dision error")
except SyntaxError as e:
    print("This is a syntax error.", e)
except:
    print("There is an exception in the input.")

finally:
    print("This block is printing no matter what because it is a finally block.")


