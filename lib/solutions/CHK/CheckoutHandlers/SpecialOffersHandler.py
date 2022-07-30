from collections import defaultdict

from .CheckoutHandler import CheckoutHandler
from ..models import Cart


class SpecialOffersHandler(CheckoutHandler):

    def __init__(self, special_offers):
        self.special_offers = special_offers

    def checkout_items(self, cart: Cart):
        items_in_specials = defaultdict(set)
        for item in cart.items:
            if item.sku in self.special_offers:
                items_in_specials[item.sku].add(item)


        for sku, sku_items in items_in_specials.items():

            special_offer = self.special_offers[sku]
            number_of_special_offers_completed = len(sku_items) // special_offer['quantity']
            number_of_items_in_offer = number_of_special_offers_completed*special_offer['quantity']

            cart.total += special_offer['price'] * number_of_special_offers_completed

            items_to_remove_from_cart = list(sku_items)[:number_of_items_in_offer]

            cart.items.difference_update(items_to_remove_from_cart)