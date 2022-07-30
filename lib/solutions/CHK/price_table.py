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
    {'item': 'A', 'price': 50},
    {'item': 'B', 'price': 30},
    {'item': 'C', 'price': 20},
    {'item': 'D', 'price': 15},
    {'item': 'E', 'price': 40},
    {'item': 'F', 'price': 10},
    {'item': 'G', 'price': 20},
    {'item': 'H', 'price': 10},
    {'item': 'I', 'price': 35},
    {'item': 'J', 'price': 60},
    {'item': 'K', 'price': 70},
    {'item': 'L', 'price': 90},
    {'item': 'M', 'price': 15},
    {'item': 'N', 'price': 40},
    {'item': 'O', 'price': 10},
    {'item': 'P', 'price': 50},
    {'item': 'Q', 'price': 30},
    {'item': 'R', 'price': 50},
    {'item': 'S', 'price': 20},
    {'item': 'T', 'price': 20},
    {'item': 'U', 'price': 40},
    {'item': 'V', 'price': 50},
    {'item': 'W', 'price': 20},
    {'item': 'X', 'price': 17},
    {'item': 'Y', 'price': 20},
    {'item': 'Z', 'price': 21}

]

special_offers = {
    'A': [{'quantity': 5, 'price': 200}, {'quantity': 3, 'price': 130}],
    'B': [{'quantity': 2, 'price': 45}],
    'F': [{'quantity': 3, 'price': 20}],
    'H': [{'quantity': 10, 'price': 80}, {'quantity': 5, 'price': 45}],
    'K': [{'quantity': 2, 'price': 120}],
    'P': [{'quantity': 5, 'price': 200}],
    'Q': [{'quantity': 3, 'price': 80}],
    'U': [{'quantity': 4, 'price': 120}],
    'V': [{'quantity': 3, 'price': 130}, {'quantity': 2, 'price': 90}],
}

bundle_assignments = {
    'B': 1,
    'E': 1,
    'N': 2,
    'M': 2,
    'R': 3,
    'Q': 3
}

bundle_offers = {
    1: {'rules': {'E': 2, 'B': 1}, 'discount': 30},
    2: {'rules': {'N': 3, 'M': 1}, 'discount': 15},
    3: {'rules': {'R': 3, 'Q': 1}, 'discount': 30}
}

any_of_offers_assignments = {
    'S': 1,
    'T': 1,
    'X': 1,
    'Y': 1,
    'Z': 1,
}


any_of_offers = {
    1: {'items': ['S','T','X','Y','Z'], 'quantity':3, 'price': 45}

}