low_price=0
medium_price=0
high_price=0

customer_served=0
total_sales=0

while True:
   name=input("Hello customer, What is your name?  ")
   item_count=int(input(f"Hello {name}, How many items do you want to buy?  "))
   if item_count<=0:
      print("Invalid grocery number. Please enter a valid number") 
      continue
   print(f"Billing for {name}")
   customer_total=0
   item_counter=1
   while item_counter<=item_count:
      print(f"item count:{item_count}")
      print(f"item counter:{item_counter}")

      item_name=input(f"Hello {name}, What is the name of item{item_counter}?  ")
      item_price=float(input(f"Hello {name}, What is the price of the item{item_counter}?  "))
      item_number=int(input(f"Hello {name}, What is the number of item{item_counter}? "))
      customer_total += item_price * item_number
      item_counter+=1
      print (f"item counter after increment {item_counter}")
      if item_price*item_number<100:
         print("This is at a low price")
      elif item_price*item_number<200:
         print("This is at a medium price")
      else:
         print("This is at a high price")
      if item_price<=0 or item_number<=0:
         print("Invalid price or quanity.Please enter correctly")
         continue
   print(name, "your total is", customer_total)


      
      
      
       