
class Item:

    def __init__(self, sku, price):
        self.sku = sku
        self.price = price


class Cart:

    total = 0
    def __init__(self, items: list[Item]):

        self.items = set(items)
