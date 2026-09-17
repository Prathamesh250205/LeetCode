class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        min_len = [float('inf')] * n
        left = 0
        current_sum = 0
        ans = float('inf')

        for right in range(n):
            current_sum += arr[right]

            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                curr_len = right - left + 1
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                
                prev_best = min_len[right - 1] if right > 0 else float('inf')
                min_len[right] = min(prev_best, curr_len)
            else:
                min_len[right] = min_len[right - 1] if right > 0 else float('inf')

        return ans if ans != float('inf') else -1