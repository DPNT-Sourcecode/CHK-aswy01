from ..models import Cart


class CheckoutHandler:

    def checkout_items(self, cart: Cart):
        cart.total += sum([item.price for item in cart.items])

    @staticmethod
    def checkout_item(cart, item):
        cart.total += item.price
        cart.items.remove(item)