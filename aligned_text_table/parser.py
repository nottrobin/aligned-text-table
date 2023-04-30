import re


class LineLengthError(Exception):
    pass


def parse_row(lines: list) -> list:
    """
    This will parse a single multi-line row of a space-aligned table into a
    list containing the text for each column.

    ```
    >>> parse_row(
    ...     lines=[
    ...         "This is     Column two   This one ",
    ...         "column one               is column",
    ...         "                         three    "
    ...     ]
    ... )

    [
        "This is column one",
        "Column two",
        "This one is column three"
    ]
    ```
    """

    first_line = lines[0]
    gutter_regex = "\s\s\s+"

    # Find column ranges
    # ===
    column_ranges = []
    start_position = 0
    gutter_match = re.search(gutter_regex, first_line)

    while gutter_match:
        new_position = start_position + gutter_match.end()
        column_ranges.append((start_position, new_position))
        gutter_match = re.search(gutter_regex, first_line[new_position:])
        start_position = new_position

    # Add the final column if it wasn't already added
    if start_position < len(first_line):
        column_ranges.append((start_position, len(first_line)))

    # Check line length
    # ===
    first_line_length = len(lines[0])
    for line in lines:
        if len(line) != first_line_length:
            raise LineLengthError(
                f"Found lines of differing lengths: {first_line_length} vs {len(line)}"
            )

    # Split line text into columns
    # ===
    columns = []
    for column_range in column_ranges:
        column_lines = []

        for line in lines:
            # Split line into columns
            start = column_range[0]
            end = column_range[1]
            column_lines.append(line[start:end].strip())

        columns.append(" ".join(column_lines).strip())

    return columns
