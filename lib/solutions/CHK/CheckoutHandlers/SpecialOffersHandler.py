from ..models import Cart


class SpecialsHandler:

    def __init__(self, special_offers):
        self.special_offers = special_offers

    def checkout_items(self, cart: Cart):
        
