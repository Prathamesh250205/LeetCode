class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        hex_digits = "0123456789abcdef"
        
        if num < 0:
            num += 2**32
        
        result = []
        while num > 0:
            result.append(hex_digits[num % 16])
            num //= 16
        
        return ''.join(reversed(result))