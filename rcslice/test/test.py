
import logging
from rcslice import RowSlice


LOGGER_NAME = 'mdx_include_test'
log = logging.getLogger(LOGGER_NAME)

def get_file_content(path):
    cont = ''
    try:
        with open(path, 'r') as f:
            cont = f.read();
    except Exception as e:
        log.exception("E: could not read file: " + path)
    return cont


ls = RowSlice(['I am a separator'])


textl = [
            'This is line 1',
            'This is line 2',
            'This is line 3',
            'This is line 4',
            'This is line 5',
            'This is line 6',
            'This is line 7',
            'This is line 8',
            'This is line 9',
        ]
lst = []
# From the end of every child sliceable to the begining of the same child(reversion)
# reverses the strings in the tesxtl list above
lst.append(ls.slice_list_of_sliceables(textl, '.-.1'))

# everything unmodified (inefficient no slice, use '' instead)
lst.append(ls.slice_list_of_sliceables(textl, '.-.'))

# From the beginning of everything to the end of everything (inefficient no slice, use '' instead)
# the result is everything unmodified
lst.append(ls.slice_list_of_sliceables(textl, '.1-.'))

# From the beginning of everything to the end of everything (inefficient no slice, use '' instead)
# the result is everything unmodified
lst.append(ls.slice_list_of_sliceables(textl, '1.1-.'))

# From the beginning of first child to the 3rd element of last child
lst.append(ls.slice_list_of_sliceables(textl, '1.1-.3'))

# From the first element of first child to the 3rd element of first child
# performs a string slice operation for the above test in first line
lst.append(ls.slice_list_of_sliceables(textl, '1.1-1.3'))

# From the 6th element of first child to the first element of first child (reversion)
lst.append(ls.slice_list_of_sliceables(textl, '1.6-1.1'))

# From the 6th element of first child to the last element of first child
lst.append(ls.slice_list_of_sliceables(textl, '1.6-1.'))

# Column slice; slice from 2nd element to 8th element on every child
lst.append(ls.slice_list_of_sliceables(textl, '.2-.8'))

# # Column slice + reversion; slice from 8nd element to 2nd element on every child
lst.append(ls.slice_list_of_sliceables(textl, '.8-.2'))

# From 8th element of last child to 2nd element of 2nd line
lst.append(ls.slice_list_of_sliceables(textl, '.8-2.2'))

# From 2nd child to the 2nd element of 3rd child
lst.append(ls.slice_list_of_sliceables(textl, '2-3.2'))

# First child
lst.append(ls.slice_list_of_sliceables(textl, '1-1'))

# From first child to last child (everything unmodified, inefficient, use '' instead)
lst.append(ls.slice_list_of_sliceables(textl, '1-'))


# ~ # From 2nd child to last child
lst.append(ls.slice_list_of_sliceables(textl, '2-'))

# From last child to first child, (reverse the list)
lst.append(ls.slice_list_of_sliceables(textl, '-1'))

# From last child to 3rd child (reversion)
lst.append(ls.slice_list_of_sliceables(textl, '-3'))

# no slice
lst.append(ls.slice_list_of_sliceables(textl, ''))

# no slice
lst.append(ls.slice_list_of_sliceables(textl, ''))

# inefficient no slice, use ''
lst.append(ls.slice_list_of_sliceables(textl, '-'))

# From the 2nd element of first child to the 8th element of last child
lst.append(ls.slice_list_of_sliceables(textl, '1.2-.8'))

# Slices from 2nd element in every child
lst.append(ls.slice_list_of_sliceables(textl, '.2-.'))

# Slices from 2nd element in every child
lst.append(ls.slice_list_of_sliceables(textl, '.2-'))

# From Last child to 2nd child
lst.append(ls.slice_list_of_sliceables(textl, '-2'))

# From last element to 2nd element in every child (reversion)
lst.append(ls.slice_list_of_sliceables(textl, '-.2'))

# From last element to 2nd element in every child (reversion)
lst.append(ls.slice_list_of_sliceables(textl, '.-.2,'))

lst.append(ls.slice_list_of_sliceables(textl, '1-2,2-3.4,3.6-1'))


lsts = str(lst)
# ~ print(lsts)
assert(lsts == get_file_content('rcslice/test/out1.txt').strip())
