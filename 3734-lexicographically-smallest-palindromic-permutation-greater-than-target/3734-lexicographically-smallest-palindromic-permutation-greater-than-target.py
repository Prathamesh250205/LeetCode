class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1

        odd_indices = [i for i in range(26) if count[i] % 2 == 1]

        # feasibility of forming any palindrome at all
        if n % 2 == 0:
            if odd_indices:
                return ""
            mid_char = None
        else:
            if len(odd_indices) != 1:
                return ""
            mid_char = chr(odd_indices[0] + 97)

        half_counts = [0] * 26
        for i in range(26):
            if mid_char is not None and i == odd_indices[0]:
                half_counts[i] = (count[i] - 1) // 2
            else:
                half_counts[i] = count[i] // 2

        half_len = n // 2
        target_half = target[:half_len]

        def counts_of(sub):
            c = [0] * 26
            for ch in sub:
                c[ord(ch) - 97] += 1
            return c


        if counts_of(target_half) == half_counts:
            forced_full = target_half + (mid_char or '') + target_half[::-1]
            if forced_full > target:
                return forced_full


        def smallest_greater_permutation(t, counts):
            L = len(t)
            cur = counts[:]
            best_i = -1
            best_char = ''
            best_remaining = None
            feasible = True

            for i in range(L):
                if not feasible:
                    break
                ti = ord(t[i]) - 97
                for c in range(ti + 1, 26):
                    if cur[c] > 0:
                        remaining_after = cur[:]
                        remaining_after[c] -= 1
                        best_i = i
                        best_char = chr(c + 97)
                        best_remaining = remaining_after
                        break
                if cur[ti] > 0:
                    cur[ti] -= 1
                else:
                    feasible = False

            if best_i == -1:
                return None

            suffix = []
            for c in range(26):
                suffix.append(chr(c + 97) * best_remaining[c])
            return t[:best_i] + best_char + ''.join(suffix)

        H = smallest_greater_permutation(target_half, half_counts)
        if H is None:
            return ""

        return H + (mid_char or '') + H[::-1]