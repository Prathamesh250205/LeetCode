class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        queue = list(range(1, 10))

        for _ in range(n - 1):
            next_queue = []
            for num in queue:
                last_digit = num % 10
                if last_digit + k <= 9:
                    next_queue.append(num * 10 + last_digit + k)
                if k != 0 and last_digit - k >= 0:
                    next_queue.append(num * 10 + last_digit - k)
            queue = next_queue

        return queue