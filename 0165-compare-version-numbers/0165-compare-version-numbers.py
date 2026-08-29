class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))

        for i in range(n):
            r1 = int(v1[i]) if i < len(v1) else 0
            r2 = int(v2[i]) if i < len(v2) else 0
            if r1 < r2:
                return -1
            if r1 > r2:
                return 1

        return 0