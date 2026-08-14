class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
        
        result = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])
        
        return result