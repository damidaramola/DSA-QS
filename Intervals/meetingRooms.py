

#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start)

        for i in range(1,len(intervals)):
            l1 = intervals[i-1][1]
            l2 = intervals[i][0]

            if l1 < l2:
                return True
        return False
         









intervals = [(0,30),(5,10),(15,20)]

test = Solution()
run = test.canAttendMeetings(intervals)
print(run)