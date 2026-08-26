class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"

        for _ in range(n - 1):
            next_result = []
            i = 0
            length = len(result)
            while i < length:
                j = i
                while j < length and result[j] == result[i]:
                    j += 1
                next_result.append(str(j - i))
                next_result.append(result[i])
                i = j
            result = ''.join(next_result)

        return result