class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)

        if k % 2 == 1:
            return parent
        else:
            return 1 - parent