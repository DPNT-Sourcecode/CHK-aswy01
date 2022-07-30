from . import price_table
from .CheckoutHandlers.AnyOfOfferHandler import AnyOfOfferHandler
from .CheckoutHandlers.BundleOffersHandler import BundleOffersHandler
from .CheckoutHandlers.CheckoutHandler import CheckoutHandler
from .CheckoutHandlers.SpecialOffersHandler import SpecialOffersHandler
from .models import Item, Cart


class ItemFactory:

    def __init__(self, item_prices: list):
        self.items_db = {}
        for item in item_prices:
            self.items_db[item['item']] = item['price']

    def get_item(self, sku):
        return Item(sku, self.items_db[sku])


items_factory = ItemFactory(price_table.item_prices)


bundleOffersHandler = BundleOffersHandler(price_table.bundle_assignments, price_table.bundle_offers)
anyOfHandler = AnyOfOfferHandler(price_table.any_of_offers_assignments, price_table.any_of_offers)
specialOffersHandler = SpecialOffersHandler(price_table.special_offers)

checkoutHandler = CheckoutHandler()


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
        shopping_cart.append(item_model)
    cart = Cart(shopping_cart)

    bundleOffersHandler.checkout_items(cart)


    specialOffersHandler.checkout_items(cart)
    # anyOfHandler.checkout_items(cart)

    checkoutHandler.checkout_items(cart)


    return cart.total
    # raise NotImplementedError()


