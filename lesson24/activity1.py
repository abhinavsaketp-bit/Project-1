items=["pencils","Pouch","lunch box","eraser"]
stock_counts=[4,7,2,0]

inventory={item:count for item,count in zip(items,stock_counts)}
print(inventory)

items_in_stock=[item for item in items if inventory[item]>0]
print(items_in_stock)

selected_item=input("Which item do you want to buy? ")
if selected_item not in inventory or inventory[selected_item]==0:
    print("Item not in Stock!: ",selected_item)
    exit()


