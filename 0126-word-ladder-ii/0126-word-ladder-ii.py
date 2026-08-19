from collections import defaultdict
import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        word_set.discard(beginWord)
        layer = {beginWord}
        parents = defaultdict(set)
        found = False
        
        while layer and not found:
            next_layer = defaultdict(set)
            for word in layer:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_set:
                            next_layer[new_word].add(word)
            
            for word in next_layer:
                if word == endWord:
                    found = True
            
            word_set -= set(next_layer.keys())
            for word, preds in next_layer.items():
                parents[word] |= preds
            layer = set(next_layer.keys())
        
        if not found:
            return []
        
        result = []
        def dfs(word, path):
            if word == beginWord:
                result.append([beginWord] + path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [word])
        
        dfs(endWord, [])
        return result