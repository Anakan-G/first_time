import os; os.system("cls")
class Expense():
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __str__(self):
        return f"Item: {self.item}\nPrice: {self.price}\n"
    
    def __add__(self, other):
        return self.price + other.price




food = Expense("food", 45)
travel = Expense("travel", 90)



print(food)
print(travel)

print("-" * 60)

# print((food + travel) + clothes)