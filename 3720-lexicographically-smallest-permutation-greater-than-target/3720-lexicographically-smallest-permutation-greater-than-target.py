class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1

        best_i = -1
        best_char = ''
        best_remaining = None

        cur = count[:]
        feasible = True

        for i in range(n):
            if not feasible:
                break
            t = ord(target[i]) - 97

            # smallest available letter strictly greater than target[i]
            for c in range(t + 1, 26):
                if cur[c] > 0:
                    remaining_after = cur[:]
                    remaining_after[c] -= 1
                    best_i = i
                    best_char = chr(c + 97)
                    best_remaining = remaining_after
                    break

            # consume target[i] to extend the matching prefix
            if cur[t] > 0:
                cur[t] -= 1
            else:
                feasible = False

        if best_i == -1:
            return ""

        suffix = []
        for c in range(26):
            suffix.append(chr(c + 97) * best_remaining[c])

        return target[:best_i] + best_char + ''.join(suffix)