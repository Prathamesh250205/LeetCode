class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m = len(s), len(p)
        if m > n:
            return []

        p_count = [0] * 26
        window_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        result = []

        for i in range(n):
            window_count[ord(s[i]) - ord('a')] += 1

            if i >= m:
                window_count[ord(s[i - m]) - ord('a')] -= 1

            if i >= m - 1 and window_count == p_count:
                result.append(i - m + 1)

        return result