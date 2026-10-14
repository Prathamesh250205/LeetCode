class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        # A positive integer of length 'num' must have a digit sum between 1 and 9 * num
        if sum < 1 or sum > 9 * num:
            return ""

        # To maximize sum of squares, greedily pick the largest possible digits (9s)
        count_9 = sum // 9
        remainder = sum % 9
        count_0 = num - count_9 - (1 if remainder > 0 else 0)

        # Form the lexicographically largest number: 9s, then remainder, then 0s
        digits = []
        digits.append('9' * count_9)
        if remainder > 0:
            digits.append(str(remainder))
        digits.append('0' * count_0)

        return "".join(digits)