class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        if len(s) < total_len:
            return []
        
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        for i in range(word_len):
            left = i
            count = 0
            window = {}
            
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                
                if word in word_count:
                    window[word] = window.get(word, 0) + 1
                    count += 1
                    
                    while window[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    window = {}
                    count = 0
                    left = j + word_len
        
        return result