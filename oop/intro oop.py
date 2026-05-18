class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, pct):
        return self.price * (1 - pct / 100)

    def sell(self, qty):
        if qty > self.stock:
            print("not enough stock")
            return self.stock
        return self.stock - qty

class Animal:
    _all_animals = []

    def __init__(self, name: str, tricks):
        self.name = name
        self.tricks = tricks

    @classmethod
    def display_all_animals(cls):
        print(cls._all_animals)