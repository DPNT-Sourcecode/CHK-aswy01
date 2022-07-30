import pytest

from solutions.HLO import hello_solution


test_examples = [
    ("John", "Hello, John!"),
    ("Mr John Doe", "Hello, Mr John Doe!")

]


class TestHello:

    @pytest.mark.parametrize('name, expected_output', test_examples)
    def test_sum(self, name, expected_output):
        assert hello_solution.hello(name) == expected_output
