import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        count = Counter(s)
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        result = []
        prev_freq, prev_ch = 0, ''

        while heap:
            freq, ch = heapq.heappop(heap)
            result.append(ch)
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_ch))
            freq += 1
            prev_freq, prev_ch = freq, ch

        if len(result) != len(s):
            return ""
        return "".join(result)