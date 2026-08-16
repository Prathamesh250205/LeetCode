from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        candidates = sorted(count.keys(), key=lambda w: (-count[w], w))
        return candidates[:k]