class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half = n // 2
        first, second = num[:half], num[half:]

        q1, q2 = first.count('?'), second.count('?')
        sum1 = sum(int(c) for c in first if c != '?')
        sum2 = sum(int(c) for c in second if c != '?')

        diff = sum1 - sum2
        totalQ = q1 + q2

        if totalQ % 2 == 1:
            return True

        return diff != 9 * (q2 - q1) // 2