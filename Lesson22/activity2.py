test_dict={"happy":2,"sad":0,"angry":3,"peaceful":2}
print(str(test_dict))

k=2

res=0
for key in test_dict.items():
    if test_dict[key]==k:
        res=+1
print("The Frequency of k is: ", str(res))