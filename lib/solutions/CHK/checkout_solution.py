
from . import price_table


def load_items(item_prices: list, special_offers: dict ):
    items_db = {}
    for item in item_prices:
        items_db['item'] = item['price']

    return items_db



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    items_db = load_items(price_table.item_prices, price_table.special_offers)
    if not skus:
        return 0
    for sku in skus:
        if sku not in items_db:
            return -1




    # raise NotImplementedError()


