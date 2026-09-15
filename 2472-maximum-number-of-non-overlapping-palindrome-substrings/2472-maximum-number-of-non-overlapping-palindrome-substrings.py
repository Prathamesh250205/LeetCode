class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        ans = 0
        last = -1

        for center in range(2 * n - 1):
            l = center // 2
            r = l + center % 2
            while l > last and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    ans += 1
                    last = r
                    break
                l -= 1
                r += 1

        return ans