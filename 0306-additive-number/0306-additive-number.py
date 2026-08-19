class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)
        
        def valid(s):
            return s == "0" or s[0] != "0"
        
        def backtrack(first, second, rest):
            if not rest:
                return True
            for i in range(1, len(rest) + 1):
                third = rest[:i]
                if not valid(third):
                    continue
                if int(third) != int(first) + int(second):
                    continue
                if backtrack(second, third, rest[i:]):
                    return True
            return False
        
        for i in range(1, n):
            first = num[:i]
            if not valid(first):
                break
            for j in range(i + 1, n):
                second = num[i:j]
                if not valid(second):
                    break
                if backtrack(first, second, num[j:]):
                    return True
        
        return False