class Solution(object):
    def findMinDifference(self, timePoints):
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(':'))
            minutes.append(h * 60 + m)
        
        minutes.sort()
        n = len(minutes)
        min_diff = float('inf')
        
        for i in range(1, n):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])
        
        return min_diff