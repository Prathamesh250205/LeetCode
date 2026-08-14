class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1

            while count[ch] > 2:
                left_ch = s[left]
                count[left_ch] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best