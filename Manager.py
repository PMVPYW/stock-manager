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

    def __str__(self):
        print(self.list)

    def add(self, name: str, quantity: int):
        for x in self.list:
            if x.name == name:
                return False
        self.list.append(Item(name, quantity))

    def remove(self, name: str):
        for x in self.list:
            if x.name == name:
                self.list.remove(x)

    def index(self, name: int):
        i = 0
        for x in self.list:
            if x.name == name:
                return i
            i+=1
        return -1