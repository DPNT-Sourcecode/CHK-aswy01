import pytest

from solutions.CHK import checkout_solution


test_examples = [
    # ('', 0),
    # ('<',-1),
    # ("A", 50),
    # ("B", 30),
    #
    # ("C", 20),
    # ("D", 15),
    # ("AAA", 130),
    # ("AAAA", 180),
    #
    # ("BB", 45),
    # ("BBB", 75),
    # ('EEB', 80),
    # ('EEBEEB', 160),
    # ('EEBE', 120),
    # ('EEBB', 110),
    # ('AAAAA', 200),
    # ('AAAAAAAA', 330),
    # ('AAAAAAAAA', 380),
    ('AAAAAEEBAAABB', 455),
    # ("BB", 45),
]


##EEB for 80
##BB for 45

class TestHello:

    @pytest.mark.parametrize('item, expected_output', test_examples)
    def test_sum(self, item, expected_output):
        assert checkout_solution.checkout(item) == expected_output
