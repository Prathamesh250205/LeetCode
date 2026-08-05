class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: [] for i in range(n)}
        for a, b in invocations:
            graph[a].append(b)
        
        suspicious = set()
        stack = [k]
        suspicious.add(k)
        
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)
        
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))
        
        return [i for i in range(n) if i not in suspicious]