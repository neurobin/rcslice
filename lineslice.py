# -*- coding: utf-8 -*-
"""Module lineslice

"""

class LineSlice(object):
    """A class to slice line column from a list of sliceables"""
    
    def __init__(self, line_slice_separator=[]):
        """
        
        Parameter
        ---------
        
        line_slice_separator    A list of entities that will be inserted between two adjacent single operation slice.
        
        """
        self.line_slice_separator = line_slice_separator

    def get_zero_index_from_one_index(self, idx):
        """Convert 1 index to zero index"""
        if idx is not None:
            idx = idx - 1
        if idx < 0:
            idx = None
        return idx
    
    def get_two_less_index(self, idx):
        """subtract 2 from index """
        if idx is not None:
            idx = idx - 2
        if idx < 0:
            idx = None
        return idx
    
    def parse_slice_string(self, slice_string):
        """Parse slice string and return a list of lists.
        
        Returned List format:

            [
                [[start.l, start.c], [end.l, end.c], [lstep, cstep]]
            ]
        
        """
        def get_lns_or_lne(n):
            """The returned list have exactly 2 elements """
            if n:
                lns = n.split('.')
            else:
                return [None, None]
            if len(lns) > 2:
                raise ValueError("Unknown Line/Column number/range (%s) passed in line slice syntax %s" % (n, slice_string,))
            print(lns)
            lns = [int(x) if x else None for x in lns]
            for i in lns:
                if i <= 0 and i is not None:
                    raise ValueError("Line/Column number/range can not be <= 0. Detected %s in line slice syntax %s" % (n, slice_string,))
            if len(lns) == 1:
                lns.append(None)
            elif len(lns) <= 0:
                raise ValueError("Unknown Line/Column number/range (%s) passed in line slice syntax %s" % (n, slice_string,))
            return lns
        
        ll = []
        for r in slice_string.split(','):
            if r:
                l = r.split('-')
                if len(l) > 2:
                    raise ValueError("Unknown Line/Column number/range (%s) passed in line slice syntax %s" % (r, slice_string,))
                l = [x if x else None for x in l]
                print(l)
                if len(l) == 1:
                    lns = get_lns_or_lne(l[0])
                    lne = [lns[0], None]
                    step = [1, 1]
                    lns = [self.get_zero_index_from_one_index(x) for x in lns]
                    # end index is exclusive, we don't need to do -1
                    # because end index is inclusive for us
                    ll.append([lns, lne, step])
                elif len(l) == 2:
                    lns = get_lns_or_lne(l[0])
                    lne = get_lns_or_lne(l[1])
                    
                    lstep = 1 if lns[0] <= lne[0] or lne[0] is None else -1
                    cstep = -1 if lns[0] == lne[0] and lne[1] < lns[1] and lne[1] is not None else 1
                    
                    lns = [self.get_zero_index_from_one_index(x) for x in lns]
                    # end index is exclusive, we don't need to do -1
                    # because end index is inclusive for us
                    
                    if lstep < 0:
                        # negative step, we need to do -2 for end index
                        lne[0] = self.get_two_less_index(lne[0])
                    if cstep < 0:
                        # negative step, we need to do -2 for end index
                        lne[1] = self.get_two_less_index(lne[1])
                        
                    ll.append([lns, lne, [lstep, cstep]])
                else:
                    raise ValueError("Unknown Line/Column number/range (%s) passed in line slice syntax %s" % (r, slice_string,))
        return ll
        
    def slice_list_of_sliceables(self, sliceables, slice_string):
        """Take slices of sliceables by slice string (e.g 1,1-4,1.2-4.7,7.8-1.5 etc.) 
        
        sliceables must not be empty
        
        """
        sidxs = self.parse_slice_string(slice_string)
        c = 0
        new_sliceables = []
        for sidx in sidxs:
            # sidx is of the format: [[start.l, start.c], [end.l, end.c], [lstep, cstep]]
            start = sidx[0]
            end = sidx[1]
            step = sidx[2]
            if c > 0:
                new_sliceables.extend(self.line_slice_separator)
            c = c + 1
            now_slice = sliceables[start[0]:end[0]:step[0]]
            if now_slice:
                if now_slice[0] is now_slice[-1]:
                    now_slice[0] = now_slice[0][start[1]:end[1]:step[1]]
                else:
                    now_slice[0] = now_slice[0][start[1]:]
                    now_slice[-1] = now_slice[-1][:end[1]]
            print(now_slice, start[0], end[0])
            new_sliceables.extend(now_slice)
            print(new_sliceables)
            # ~ print(sidx)
        
        return new_sliceables if new_sliceables else sliceables

