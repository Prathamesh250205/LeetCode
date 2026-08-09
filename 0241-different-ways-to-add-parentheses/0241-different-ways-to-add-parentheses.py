class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]
            if expr.isdigit():
                return [int(expr)]

            results = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i + 1:])
                    for l in left:
                        for r in right:
                            if ch == "+":
                                results.append(l + r)
                            elif ch == "-":
                                results.append(l - r)
                            else:
                                results.append(l * r)

            memo[expr] = results
            return results

        return compute(expression)