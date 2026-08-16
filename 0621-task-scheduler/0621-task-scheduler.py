from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)
        max_count = max(counts.values())
        max_count_freq = sum(1 for c in counts.values() if c == max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_freq)