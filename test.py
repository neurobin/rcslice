
from lineslice import LineSlice

ls = LineSlice()


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

print(ls.slice_list_of_sliceables(textl, '2-1'))
