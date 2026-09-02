import bisect

class Solution(object):
    def findRightInterval(self, intervals):
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        start_vals = [s[0] for s in starts]
        
        res = []
        n = len(intervals)
        for _, end in intervals:
            idx = bisect.bisect_left(start_vals, end)
            if idx < n:
                res.append(starts[idx][1])
            else:
                res.append(-1)
                
        return res