class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        removals = 0
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1
                
        return removals