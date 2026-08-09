class Solution(object):
    def kthCharacter(self, k):
        index = k - 1
        shift = bin(index).count("1")
        return chr(ord('a') + shift % 26)