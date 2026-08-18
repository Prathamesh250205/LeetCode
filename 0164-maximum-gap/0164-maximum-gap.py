class Solution(object):
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        
        lo, hi = min(nums), max(nums)
        if lo == hi:
            return 0
        
        bucket_size = max(1, (hi - lo) // (n - 1))
        bucket_count = (hi - lo) // bucket_size + 1
        
        bucket_min = [None] * bucket_count
        bucket_max = [None] * bucket_count
        
        for num in nums:
            idx = (num - lo) // bucket_size
            if bucket_min[idx] is None or num < bucket_min[idx]:
                bucket_min[idx] = num
            if bucket_max[idx] is None or num > bucket_max[idx]:
                bucket_max[idx] = num
        
        max_gap = 0
        prev_max = lo
        
        for i in range(bucket_count):
            if bucket_min[i] is None:
                continue
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        
        return max_gap