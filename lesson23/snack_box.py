snack_box1={"Cookies","Dates","Juice"}
snack_box2={"Dark Chocolate","Banana","Milkshake","Banana"}
print("Snack box 1: ", snack_box1)
print("Snack box 2", snack_box2)

snack_box1.add("Banana")
print("Snack_box1 after adding___: ", snack_box1)

same=snack_box1.intersection(snack_box2)
print("The things that match in both snack box 1 and snack box 2 : ", same)

import array
snack_count=array.array('i',[2,6,7,9,4,3])
print("Snack count:", snack_count)

snack_count.insert(3,7)
print(snack_count)
snack_count.append(0)
print(snack_count)

count_of_num_7=snack_count.count(7)
print("The count of number 7 is:", count_of_num_7)

reversed=snack_count.reverse()
print("The reversed version of snack counts is:", reversed)


print("snack box 1:", snack_box1)
print("Sanck box 2:", snack_box2)
print("Matching snacks:", same)
print("Final snacks count:", snack_count)
