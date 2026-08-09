class Solution(object):
    def allPossibleFBT(self, n):
        memo = {}

        def build(n):
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]

            results = []
            for left_count in range(1, n, 2):
                right_count = n - 1 - left_count
                left_trees = build(left_count)
                right_trees = build(right_count)
                for l in left_trees:
                    for r in right_trees:
                        results.append(TreeNode(0, l, r))

            memo[n] = results
            return results

        return build(n)