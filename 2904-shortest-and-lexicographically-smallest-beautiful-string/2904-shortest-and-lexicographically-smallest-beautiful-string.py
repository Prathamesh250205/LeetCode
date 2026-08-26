class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        best_len = float('inf')
        best = ""
        left = 0
        ones = 0

        for right in range(n):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:

                while s[left] == '0':
                    left += 1
                length = right - left + 1
                candidate = s[left:right + 1]
                if length < best_len or (length == best_len and candidate < best):
                    best_len = length
                    best = candidate

        return best