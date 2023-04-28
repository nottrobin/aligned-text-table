# Aligned text table

A parser for tables in plain text that are aligned with spaces, e.g.:

```
This is     Column two   This one
column one               is column
                         three
```

## Usage

```
>>> from aligned_text_table import parse_row

>>> parse_row(
...     lines=[
...         "This is     Column two   This one ",
...         "column one               is column",
...         "three    "
...     ],
...     keys=["one", "two", "three"]
... )

{
    "one": "This is column one",
    "two": "Column two",
    "three": "This one is column three"
}
```

## Tests

To run tests, install and run Tox:

```
pip3 install tox
tox
```
