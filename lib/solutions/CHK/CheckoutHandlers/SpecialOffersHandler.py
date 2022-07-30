from .CheckoutHandler import CheckoutHandler
from ..models import Cart


class SpecialsHandler(CheckoutHandler):

    def __init__(self, special_offers):
        self.special_offers = special_offers

    def checkout_items(self, cart: Cart):

        for item in cart.items:
            if item.sku