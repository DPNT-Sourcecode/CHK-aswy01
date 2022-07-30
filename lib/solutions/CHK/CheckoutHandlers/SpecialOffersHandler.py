from collections import defaultdict

from .CheckoutHandler import CheckoutHandler
from ..models import Cart


class SpecialsHandler(CheckoutHandler):

    def __init__(self, special_offers):
        self.special_offers = special_offers

    def checkout_items(self, cart: Cart):
        items_in_specials = defaultdict(set)
        for item in cart.items:
            if item.sku in self.special_offers:
                items_in_specials[item.sku].add(item)


        for sku, sku_items in items_in_specials.items():

            for special_offer in self.special_offers[sku]:
