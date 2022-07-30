from . import price_table
from .models import Item, Cart


class ItemFactory:

    def __init__(self, item_prices: list):
        self.items_db = {}
        for item in item_prices:
            self.items_db['item'] = item['price']

    def get_item(self, sku):
        return Item(sku, self.items_db[sku])


items_factory = ItemFactory(price_table.item_prices)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not skus:
        return 0
    for sku in skus:
        if sku not in items_factory.items_db:
            return -1

    shopping_cart = []
    for item in list(skus):
        item_model = items_factory.get_item(item)

    cart = Cart(shopping_cart)



    # raise NotImplementedError()





