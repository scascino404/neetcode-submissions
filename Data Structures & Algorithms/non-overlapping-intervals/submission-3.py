class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        INF = 100_000

        intervals.sort(key=lambda x: x[1])

        prev_end = -INF
        erased = 0
        for start, end in intervals:
            if start < prev_end:
                erased += 1
            else:
                prev_end = end
    
        return erased
