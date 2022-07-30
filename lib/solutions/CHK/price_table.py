# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# +------+-------+------------------------+


item_prices = [
    {'item':'A', 'price': 50},
    {'item':'B', 'price': 30},
    {'item':'C', 'price': 20},
    {'item':'D', 'price': 15},
    {'item': 'E', 'price': 40},
    {'item': 'F', 'price': 10},
    {'item': 'G', 'price': 20},
    {'item': 'H', 'price': 10},
    {'item': 'I', 'price': 35},
    {'item': 'J', 'price': 60},
    {'item': 'K', 'price': 80},
    {'item': 'L', 'price': 90},
    {'item': 'M', 'price': 15},
    {'item': 'N', 'price': 40},
    {'item': 'O', 'price': 10},
    {'item': 'P', 'price': 50},
    {'item': 'Q', 'price': 30},
    {'item': 'R', 'price': 50},
    {'item': 'S', 'price': 30},
    {'item': 'T', 'price': 2},
    {'item': 'U', 'price': 10},
    {'item': 'V', 'price': 10},
    {'item': 'W', 'price': 10},
    {'item': 'X', 'price': 10},
    {'item': 'Y', 'price': 10},
    {'item': 'Z', 'price': 10}

]

special_offers = {
    'A': [{'quantity': 5, 'price': 200},{'quantity': 3, 'price': 130}],
    'B': [{'quantity': 2, 'price': 45}],
    'F': [{'quantity': 3, 'price': 20}]
}

bundle_assignments = {
    'B': 1,
    'E': 1
}

bundle_offers = {
    1: {'rules': {'E': 2, 'B': 1}, 'discount': 30}

}
