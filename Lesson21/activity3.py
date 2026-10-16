weather=(0,0,1,1,0,1,0)
for i in range(0,8):
    if weather[i]==0:
        rainy+=1
    sunny+=1
if sunny>rainy:
    print("The weather is great outside! you might wan to go out for a walk")
else:
    print("The weather is rainy! you better not go outside.")