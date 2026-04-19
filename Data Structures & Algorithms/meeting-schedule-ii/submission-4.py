"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]

        starts.sort()
        ends.sort()

        i = 0
        j = 0

        res = 0

        while i < len(starts):
            while i + 1 < len(starts) and starts[i + 1] < ends[j]:
                i += 1

            res = max(res, i - j + 1)

            i += 1
            j += 1

        return res

        

            
