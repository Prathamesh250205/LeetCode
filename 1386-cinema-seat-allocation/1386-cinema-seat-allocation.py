from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        row_masks = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                row_masks[row] |= 1 << (seat - 2)
        
        left_block = 0b00001111
        mid_block = 0b00111100
        right_block = 0b11110000
        
        total = (n - len(row_masks)) * 2
        
        for mask in row_masks.values():
            if (mask & left_block) == 0 and (mask & right_block) == 0:
                total += 2
            elif (mask & left_block) == 0 or (mask & mid_block) == 0 or (mask & right_block) == 0:
                total += 1
        
        return total