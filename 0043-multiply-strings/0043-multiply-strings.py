class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2
                
                pos_low = i + j + 1
                pos_high = i + j
                
                total = product + result[pos_low]
                result[pos_low] = total % 10
                result[pos_high] += total // 10
        
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0')