def intro(n):
    if n<=0:
        return
    print(n)
    intro(n-1)
num=int(input("Enter a number in which the sequence will start with: "))


intro(num)

print("https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2/")


       
