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
        ##5 As for 200
        ## 3 As for 130

        for sku, sku_items in items_in_specials.items():



            for special_offer in self.special_offers[sku]:
                number_of_items_in_special_offers = 0
                # special_offer = self.special_offers[sku]
                number_of_special_offers_completed = len(sku_items) // special_offer['quantity']
                number_of_items_in_offer = number_of_special_offers_completed*special_offer['quantity']
                number_of_items_in_special_offers+=number_of_items_in_offer
                cart.total += special_offer['price'] * number_of_special_offers_completed

                items_to_remove_from_cart = list(sku_items)[:number_of_items_in_offer]

                cart.items.difference_update(items_to_remove_from_cart)
                sku_items.difference_update(items_to_remove_from_cart)

        print('done')
