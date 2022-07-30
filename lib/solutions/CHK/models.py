from dataclasses import dataclass
from typing import Set


class Item:

    def __init__(self, sku, price):
        self.sku = sku
        self.price = price


@dataclass
class Cart:
    items: Set[Item]
    total = 0

    def __init__(self, items: list[Item]):
        self.items = set(items)
