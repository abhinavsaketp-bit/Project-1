List=[23,68,34,90]
print(List)
List.append(99)
print(List)
List.append("End")
print(List)
List.append("Entry")
print(List)
print("The element for fourth index is:", List[4])
print(List[2:6])
print(List)

for i in List:
    print(i)
List.reverse()
print(List)