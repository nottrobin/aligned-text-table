# Standard library
import unittest

# Local
from aligned_text_table import parse_row


class TestParser(unittest.TestCase):
    def test_example_table(self):
        expected = {
            "one": "This is column one",
            "two": "Column two",
            "three": "This one is column three of 3"
        }

        result = parse_row(
            lines=[
                "This is     Column two   This one  ",
                "column one               is column ",
                "three of 3"
            ],
            keys=["one", "two", "three"]
        )
    
        assert result == expected

    def test_extra_data(self):
        expected = {
            "one": "Col 1",
            "two": "Col 2",
            "three": "Col 3",
            "notes": ["NOTE: Hello world this is robin"]
        }

        result = parse_row(
            lines=[
                "Col 1     Col 2   Col 3",
                "NOTE: Hello world this is robin"
            ],
            keys=["one", "two", "three"],
            unmatched_key="notes"
        )
    
        assert result == expected
