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
    # ('Z', 21),
    # ('H'*5,45),
    # ('H'*10, 80),
    # ('V'*5,220),
    #
    # ("AAA", 130),
    # ("AAAA", 180),
    # ('K'*2, 120),
    # ('K', 70),
    # ("BB", 45),
    # ("BBB", 75),
    # ('EEB', 80),
    # ('EEBEEB', 160),
    # ('EEBE', 120),
    # ('EEBB', 110),
    # ('AAAAA', 200),
    # ('AAAAAAAA', 330),
    # ('AAAAAAAAA', 380),
    # ('AAAAAEEBAAABB', 455),
    # ("BB", 45),
    # ("FF", 20),
    # ("FFF", 20),
    # ("AFFF", 70),

    ("STX", 45),
    # ("XYZ", 45),
    # ("STXXYZ", 45),
]



##EEB for 80
##BB for 45

class TestHello:

    @pytest.mark.parametrize('item, expected_output', test_examples)
    def test_checkout(self, item, expected_output):
        assert checkout_solution.checkout(item) == expected_output


