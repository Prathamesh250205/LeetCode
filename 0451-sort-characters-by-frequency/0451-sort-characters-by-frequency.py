class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        sorted_chars = sorted(count.items(), key=lambda x: -x[1])
        
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
        
        return ''.join(result)