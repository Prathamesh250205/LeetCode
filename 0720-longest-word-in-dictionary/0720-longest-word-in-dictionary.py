class Solution(object):
    def longestWord(self, words):
        word_set = set(words)
        words.sort()
        built = {""}
        best = ""
        
        for word in words:
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(best):
                    best = word
        
        return best