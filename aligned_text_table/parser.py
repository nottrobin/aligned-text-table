import re


def parse_row(
    lines: list, keys: list,
    unmatched_key: str = "unmatched"
) -> dict:
    """
    This will parse a single multi-line row of a space-aligned table into a
    Python dictionary containing the data mapped to the provided `keys`.

    NB: Currently this function starts parsing from the *right*.

    ```
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
    """

    first_line = lines[0]
    column_data = {}

    # Find column locations
    column_ranges = []
    start_position = 0
    gutter_match = re.search("\s\s+", first_line)

    while(gutter_match):
        new_position = start_position + gutter_match.end()
        column_ranges.append( (start_position, new_position) )
        gutter_match = re.search("\s\s+", first_line[new_position:])
        start_position = new_position

    # Add the final column if it wasn't already added
    if start_position < len(first_line):
        column_ranges.append( (start_position, len(first_line)) )

    if len(column_ranges) != len(keys):
        raise ValueError(
            "The number of keys provided doesn't match the number of columns"
        )

    # Check lines
    unmatched = []
    for index, line in enumerate(lines):
        # Add spaces to start of short lines
        if len(lines[index]) < len(first_line):
            difference = len(first_line) - len(lines[index])
            lines[index] = difference * " " + lines[index]
        
        # Remove lines without gutters
        if not re.search("\s\s+", lines[index]):
            unmatched.append(lines[index])
            del lines[index]

    if unmatched:
        column_data[unmatched_key] = unmatched

    # Split into columns
    for index, key in enumerate(keys):
        column_lines = []

        for line in lines:
            # Split line into columns
            start = column_ranges[index][0]
            end = column_ranges[index][1]
            column_lines.append(line[start:end].strip())

        column_data[key] = " ".join(column_lines).strip()

    return column_data
