"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        timeline = []
        for interval in intervals:
            timeline.append((interval.start,1))
            timeline.append((interval.end, -1))
        timeline.sort()

        count = 0
        for _, event in timeline:
            assert count >= 0
            count += event
            if count > 1:
                return False
        
        return True