class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}
        
        for char in magazine:
            count[char] = count.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        return True