class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        s = list(s)
        n = len(s)

        length = [0] * (4 * n)
        lc = [''] * (4 * n)
        rc = [''] * (4 * n)
        prefix = [0] * (4 * n)
        suffix = [0] * (4 * n)
        best = [0] * (4 * n)

        def pull(node, l, mid, r):
            left, right = 2 * node, 2 * node + 1
            length[node] = length[left] + length[right]
            lc[node] = lc[left]
            rc[node] = rc[right]

            prefix[node] = prefix[left]
            if prefix[left] == length[left] and lc[left] == lc[right]:
                prefix[node] = length[left] + prefix[right]

            suffix[node] = suffix[right]
            if suffix[right] == length[right] and rc[right] == rc[left]:
                suffix[node] = length[right] + suffix[left]

            best[node] = max(best[left], best[right])
            if rc[left] == lc[right]:
                best[node] = max(best[node], suffix[left] + prefix[right])

        def build(node, l, r):
            if l == r:
                length[node] = 1
                lc[node] = rc[node] = s[l]
                prefix[node] = suffix[node] = best[node] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            pull(node, l, mid, r)

        def update(node, l, r, idx, ch):
            if l == r:
                lc[node] = rc[node] = ch
                length[node] = 1
                prefix[node] = suffix[node] = best[node] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            pull(node, l, mid, r)

        build(1, 0, n - 1)

        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            res.append(best[1])
        return res