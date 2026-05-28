class foodItem:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def calculateBill(self, quantity):
        return quantity * self.price



class vegItem(foodItem):
    def calculateBill(self, quantity):
        base = super().calculateBill(quantity)
        return base * 0.9


class nonvegItem(foodItem):
    def calculateBill(self, quantity):
        base = super().calculateBill(quantity)
        return base + 50


class beverages(foodItem):
    def calculateBill(self, quantity):
        base = super().calculateBill(quantity)
        return base - 20


orders = [
    vegItem("panner", 200),
    nonvegItem("biriyani", 300),
    beverages("coco-cola", 100),
]
for items in orders:
    print("Item name", items.calculateBill(2))
