# Polymorphism
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price


class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def get_price(self):
        shipping_cost = 5 * self.weight
        return self.price + shipping_cost


class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def get_price(self):
        # 10% discount for digital products
        discount = 0.10 * self.price
        return self.price - discount

book = PhysicalProduct("Hardcover Book", 20, weight=2)
ebook = DigitalProduct("E-Book", 15, file_size=50)

print(book.get_price())  # 20 + (5 * 2) = 30
print(ebook.get_price()) # 15 - (0.10 * 15) = 13.5
