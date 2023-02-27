class Item:
    def __init__(self ,name: str, quantity: int):
        self.name = name
        self.quantity = quantity


    def increment(self, i: int):
        self.quantity+=i

    def decrement(self, i: int):
        self.quantity-=i

class Manager:
    def __init__(self):
        self.list = []

    def add(self, name: str, quantity: int):
        for x in self.list:
            if x.name == name:
                return
        self.list.append(Item(name, quantity))