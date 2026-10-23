basket1={"apple","banana","apple", "mango"}
basket2={"Kiwi","watermelon","banana","Kiwi"}
print(basket1)
print(basket2)

basket1.add("Kiwi")
print(basket1)

common=basket1.intersection(basket2)
print(common)

import array
count1=array.array("i",[8,4,9,2,6,8])

count1.append(0)
count1.insert(3,7)
print(count1)

count1.count(8)

count1.reverse()
print(count1)

print(basket1)
print(basket2)
print(common)
print(count1)
