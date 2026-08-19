class Solution(object):
    def restoreIpAddresses(self, s):
        result = []
        n = len(s)
        
        def valid(segment):
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255
        
        def backtrack(start, path):
            if len(path) == 4:
                if start == n:
                    result.append('.'.join(path))
                return
            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start+length]
                if valid(segment):
                    path.append(segment)
                    backtrack(start + length, path)
                    path.pop()
        
        backtrack(0, [])
        return result