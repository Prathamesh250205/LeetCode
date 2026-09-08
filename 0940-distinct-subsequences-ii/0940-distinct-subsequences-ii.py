class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        end = [0] * 26
        
        for ch in s:
            idx = ord(ch) - ord('a')
            end[idx] = (sum(end) + 1) % MOD
            
        return sum(end) % MOD