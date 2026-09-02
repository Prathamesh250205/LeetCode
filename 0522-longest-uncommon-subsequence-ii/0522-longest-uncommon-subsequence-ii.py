class Solution(object):
    def findLUSlength(self, strs):
        def is_subsequence(s1, s2):
            i = 0
            for char in s2:
                if i < len(s1) and s1[i] == char:
                    i += 1
            return i == len(s1)

        strs.sort(key=len, reverse=True)
        
        for i, s1 in enumerate(strs):
            if all(not is_subsequence(s1, s2) for j, s2 in enumerate(strs) if i != j):
                return len(s1)
                
        return -1