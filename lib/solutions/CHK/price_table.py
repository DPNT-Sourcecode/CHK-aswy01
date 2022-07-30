# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


item_prices = [
    {'item':'A', 'price': 50},
    {'item':'B', 'price': 30},
    {'item':'C', 'price': 20},
    {'item':'D', 'price': 15},
    {'item': 'E', 'price': 40},
]

special_offers = {
    'A': [{'quantity': 5, 'price': 200},{'quantity': 3, 'price': 130}],
    'B': [{'quantity': 2, 'price': 45}]
}

bundle_assignments = {
    'B': 1,
    'E': 1
}

bundle_offers = {
    1: {'rules': {'E': 2, 'B': 1}, 'discount': 30}

}