# class foodItem:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def calculateBill(self, quantity):
#         return quantity * self.price



# class vegItem(foodItem):
#     def calculateBill(self, quantity):
#         base = super().calculateBill(quantity)
#         return base * 0.9


# class nonvegItem(foodItem):
#     def calculateBill(self, quantity):
#         base = super().calculateBill(quantity)
#         return base + 50


# class beverages(foodItem):
#     def calculateBill(self, quantity):
#         base = super().calculateBill(quantity)
#         return base - 20


# orders = [
#     vegItem("panner", 200),
#     nonvegItem("biriyani", 300),
#     beverages("coco-cola", 100),
#     print("i love you ")
# ]
# for items in orders:
#     print("Item name", items.calculateBill(2))





# You are using Python
# You are using Python
class foodItem:
    def __init__(self,name,price):
        self.name= name
        self.price=price
    def calculateBill(self,quantity):
        return self.price*quantity
        
class vegItems(foodItem):
    def __init__(self,name,price):
            super().__init__(name,price)
            
    def calculateBill(self,quantity):
        base=super().calculateBill(quantity)/100
        return base*10
        
class nonVegItems(foodItem):
    def __init__(self,name,price):
            super().__init__(name,price)
            
    def calculateBill(self,quantity):
        base=super().calculateBill(quantity)/100
        return base+50
        
class Beverages(foodItem):
    def __init__(self,name,price):
        super().__init__(name,price)
            
    def calculateBill(self,quantity):
        base=super().calculateBill(quantity)/100
        return (base*20)*2
        
itemCount=int(input())


orders=[]
if 1 <= itemCount <= 50:
 for i in range(itemCount):
    itemType ,name,price=input().split()
    price=int(price)
    if 1 <= price <= 1000:


        if itemType=="eg":
            orders.append(vegItems(name,price))
        elif itemType=="NonVeg":
            orders.append(nonVegItems(name,price))
        elif itemType=="Beverages":
            orders.append(Beverages(name,price  ))
quantity=int(input())
if 1 <= quantity <= 20:

 for item in orders:
        print(item.name,"Bill for ",quantity,"items:",item.calculateBill(quantity))
 


