class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_h = max(heights)
        count = [0] * (max_h + 1)
        for h in heights:
            count[h] += 1

        expected = []
        for h in range(max_h + 1):
            expected.extend([h] * count[h])

        return sum(1 for a, b in zip(heights, expected) if a != b)