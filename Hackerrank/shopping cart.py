class Item:
    def _init_(self, name: str, price: int):
        self.name = name
        self.price = price

class ShoppingCart:
    def _init_(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def total(self) -> int:
        return sum(item.price for item in self.items)

    def _len_(self):
        return len(self.items)

# Sample Input Reading
n = int(input())  # Number of items
items = []
for _ in range(n):
    name, price = input().split()
    items.append(Item(name, int(price)))

q = int(input())  # Number of operations
cart = ShoppingCart()

# Perform operations
for _ in range(q):
    operation = input().split()

    if operation[0] == 'add':
        item_name = operation[1]
        item_to_add = next(item for item in items if item.name == item_name)
        cart.add(item_to_add)
    elif operation[0] == 'len':
        print(len(cart))
    elif operation[0] == 'total':
        print(cart.total())