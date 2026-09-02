class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        arrows = 1
        prev_end = points[0][1]
        
        for start, end in points[1:]:
            if start > prev_end:
                arrows += 1
                prev_end = end
                
        return arrows