class Solution(object):
    def validSequence(self, word1, word2):
        n, m = len(word1), len(word2)
        suf = [0] * (n + 1)
        p = m
        for i in range(n - 1, -1, -1):
            if p > 0 and word1[i] == word2[p - 1]:
                p -= 1
            suf[i] = m - p

        ans = []
        i = j = 0
        used = False
        while i < n and j < m:
            if word1[i] == word2[j]:
                ans.append(i)
                i += 1
                j += 1
            elif not used and suf[i + 1] >= m - j - 1:
                ans.append(i)
                i += 1
                j += 1
                used = True
            else:
                i += 1

        if j < m:
            return []
        return ans