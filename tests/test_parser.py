# Standard library
import unittest

# Local
from aligned_text_table import parse_row


class TestParser(unittest.TestCase):
    def test_example_table(self):
        expected = {
            "One": "This is column one",
            "Two": "Column  two",
            "Three": "This one is column three of 3"
        }

        result = parse_row(
            lines=[
                "This is     Column  two   This one  ",
                "column one               is column ",
                "three of 3"
            ],
            keys=["One", "Two", "Three"]
        )
    
        assert result == expected
