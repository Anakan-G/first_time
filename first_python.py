# Anakan Gopalan
# 7/13/2023
# This program calculates the sum of 3-4 products for a computer including the taxes and shipping


print("Lets build a computer!")
print()
print()
item1 = input("What is item 1?")
cost1 = float(input("How much is item 1?"))
item2 = input("What is item 2?")
cost2 = float(input("How much is item 2?"))
item3 = input("What is item 3?")
cost3 = float(input("How much is item 3?"))
item4 = input("What is item 4? (Optional, put 0 for nothing)")
cost4 = float(input("How much is item 4? (Optional, put 0 for nothing)"))
print("Item                            Cost")
print( item1 + ":                          " + str(cost1))
print( item2 + ":                          " + str(cost2))
print( item3 + ":                          " + str(cost3))
if item4 == 0:
    print( item4 + ":                          " + str(cost4))
subTotal = cost1 + cost2 + cost3 + cost4
taxes = subTotal * 0.065
shipping = 5.99
total = subTotal + taxes + shipping
print("Subtotal")
print(str(subTotal))
print("----------------------------------------------------")
print("Taxes")
print(str(round(taxes,2)))
print("Shipping")
print(shipping)
print("Total")
print(str(round(total,2)))
print("Thank you for spending " + str(round(total,2)) +  " at Lets build a computer!. How was your service today, please rate us on a 1-5 scale.")
rating = int(input("How was the service? (1-5)"))
if rating >= 3:
    print("Thank you!")
else: print("Sorry, hopefully it will be better next time.")
