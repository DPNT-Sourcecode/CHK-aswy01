
from . import price_table
from .models import Item

class ItemFactory:
    def load_items(item_prices: list, special_offers: dict ):
        items_db = {}
        for item in item_prices:
            items_db['item'] = item['price']

        return items_db

    def get_item(self, sku):
        

items_db = load_items(price_table.item_prices, price_table.special_offers)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:


    if not skus:
        return 0
    for sku in skus:
        if sku not in items_db:
            return -1


    for item in list(skus):
        item_model = Item()



    # raise NotImplementedError()



