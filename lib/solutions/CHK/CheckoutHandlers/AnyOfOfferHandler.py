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

        for sku, sku_items in items_in_specials.items():
            bundle_offer = self.bundle_offers[sku]

            number_of_complete_bundles = math.inf
            for req_sku, count in bundle_offer['rules'].items():
                max_offers_complete_for_sku = len(list(filter(lambda i: i.sku == req_sku, sku_items))) // count

                if max_offers_complete_for_sku < number_of_complete_bundles:
                    number_of_complete_bundles = max_offers_complete_for_sku

            cart.total -= bundle_offer['discount'] * number_of_complete_bundles

            for (item_sku, items_for_sku) in groupby(sorted((sku_items),key=lambda i: i.sku), key=lambda i: i.sku):
                number_of_items_to_remove = number_of_complete_bundles * bundle_offer['rules'][item_sku]
                items_for_sku = list(items_for_sku)
                for item in list(items_for_sku)[:number_of_items_to_remove]:
                    CheckoutHandler.checkout_item(cart, item)
