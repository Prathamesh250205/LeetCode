class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)
        order = sorted(range(n), key=lambda i: score[i], reverse=True)
        answer = [""] * n
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for rank, idx in enumerate(order):
            if rank < 3:
                answer[idx] = medals[rank]
            else:
                answer[idx] = str(rank + 1)
        return answer