class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return result