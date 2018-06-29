import unittest
from operator import itemgetter

def merge_ranges(meetings):
    if len(meetings) <= 1:
        return meetings

    meetings = sorted(meetings, key=itemgetter(0))
    pdl = [meetings[0]]
    meetings = meetings[1:]
    for (nstart, nend) in meetings:
        (start, end) = pdl[-1]
        if nstart <= end:
            if end <= nend:
                end = nend
            pdl[-1] = (start, end)
        else:
            pdl.append((nstart, nend))
    return pdl
