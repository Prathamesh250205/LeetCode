import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        max_radius = 0
        n = len(heaters)
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            
            dist1 = abs(heaters[idx] - house) if idx < n else float('inf')
            dist2 = abs(heaters[idx - 1] - house) if idx > 0 else float('inf')
            
            closest = min(dist1, dist2)
            max_radius = max(max_radius, closest)
            
        return max_radius