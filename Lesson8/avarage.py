a=int(input("enter a value for a: "))
b=int(input("Enter a value for b: "))
c=int(input("Enter a value for c: "))
total=a+b+c
average=total/3
print("The average of the numbers is", average)
if average>a and average>b and average>c:
    print("Average is greater than a,b and c.")
elif average>a and average>b:
    print("Average is greater than a and b")
elif average>b and average>c:
    print("Average is greater than b and c")
elif average>a and average>c:
    print("Average is greater than a and c")
else:
    print("None of the statments satisfied")