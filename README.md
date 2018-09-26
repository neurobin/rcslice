[![Build Status](https://travis-ci.org/neurobin/rcslice.svg?branch=release)](https://travis-ci.org/neurobin/rcslice)


This package provides Python module to slice a list of sliceables (1 indexed, both start and end index are inclusive). Helps to slice file content line by line or column by column or a combination of both.

# Install

Install from Pypi:

```bash
pip install rcslice
```

# Usage

```python
from rcslice import RowSlice

rs = RowSlice()

list_of_sliceables = rs.slice_list_of_sliceables(list_of_sliceables, slice_string)

```

# Slicing syntax

Below, r is the row number (inclusive, 1 indexed), and c is the column number (inclusive, 1 indexed)

    r.c-r.c
    r.c-r.c,r.c-r.c,...
    r-r         [not specifying c means the last c (always)]
    .c-.c       [not specifying both r means slice on every row for the columns]
    1.c-.c      [not specifying r means the last row when another r is specified]
    .c-1        [last row.c to first row, reversion]
            


Reversion, row wise or column wise or a mix of two are allowed.

        

# Examples

An example of slicing a file content read by `readlines()`:

```python

import os
from rcslice import RowSlice

def get_file_lines(filename):
    content = []
    try:
        with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
            content = f.readlines()
    except OSError as e:
        raise
    return content


rs = RowSlice(['','']) # ['',''] will add 2 new lines for multi slice syntax (e.g 1-2,3-4,...)

list_of_lines = get_file_lines('test.txt')

print("before: ", list_of_lines)

list_of_lines = rs.slice_list_of_sliceables(list_of_lines, '1-2,1.2-4.5,3.4-1.3,.4-.9')

print("after: ", list_of_lines)

```
