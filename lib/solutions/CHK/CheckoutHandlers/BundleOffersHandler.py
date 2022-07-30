import math
from collections import defaultdict

from .CheckoutHandler import CheckoutHandler
from ..models import Cart


class BundleOffersHandler(CheckoutHandler):

    def __init__(self, bundle_assignments, bundle_offers):

        self.bundle_assignments = bundle_assignments
        self.bundle_offers = bundle_offers

    def checkout_items(self, cart: Cart):
        items_in_specials = defaultdict(set)
        for item in cart.items:
            if item.sku in self.bundle_assignments:
                bundle_assigned = self.bundle_assignments[item.sku]
                items_in_specials[bundle_assigned].add(item)

        for sku, sku_items in items_in_specials.items():
            bundle_offer = self.bundle_offers[sku]

            number_of_complete_bundles = math.inf
            for req_sku, count in bundle_offer['rules'].items():
                max_offers_complete_for_sku = len(list(filter(lambda i: i.sku == req_sku, sku_items))) // count

                if max_offers_complete_for_sku < number_of_complete_bundles:
                    number_of_complete_bundles = max_offers_complete_for_sku

            cart.total -= bundle_offer['discount'] * number_of_complete_bundles

            number_of_special_offers_completed = len(sku_items) // special_offer['quantity']
            number_of_items_in_offer = number_of_special_offers_completed * special_offer['quantity']

            cart.total += special_offer['price'] * number_of_special_offers_completed

            items_to_remove_from_cart = list(sku_items)[:number_of_items_in_offer]

            cart.items.difference_update(items_to_remove_from_cart)


