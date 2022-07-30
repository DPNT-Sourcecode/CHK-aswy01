import math
from collections import defaultdict

from .CheckoutHandler import CheckoutHandler
from ..models import Cart


class AnyOfOfferHandler(CheckoutHandler):

    def __init__(self, bundle_assignments, bundle_offers):

        self.bundle_assignments = bundle_assignments
        self.bundle_offers = bundle_offers

    def checkout_items(self, cart: Cart):
        items_in_specials = defaultdict(list)
        for item in cart.items:
            if item.sku in self.bundle_assignments:
                bundle_assigned = self.bundle_assignments[item.sku]
                items_in_specials[bundle_assigned].append(item)

        for group_id, sku_items in items_in_specials.items():
            bundle_offer = self.bundle_offers[group_id]
            bundle_quantity = bundle_offer['quantity']

            number_of_complete_bundles = len(items_in_specials) // bundle_quantity

            for i in list(sorted(sku_items, key=lambda e: e.price, reverse=True))[
                     :number_of_complete_bundles * bundle_quantity]:
                cart.items.remove(i)

            cart.total += bundle_offer['price'] * number_of_complete_bundles


