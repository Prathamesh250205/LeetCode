from itertools import permutations


class Solution(object):
    def totalNumbers(self, digits):
        results = set()
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            if perm[2] % 2 != 0:
                continue
            results.add(perm[0] * 100 + perm[1] * 10 + perm[2])
        return len(results)