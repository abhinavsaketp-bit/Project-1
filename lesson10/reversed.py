string=input("Enter a string value: ")

number=len(string)
answer=""
for i in range(0,number):
    answer= string[i]+answer
print(answer)


