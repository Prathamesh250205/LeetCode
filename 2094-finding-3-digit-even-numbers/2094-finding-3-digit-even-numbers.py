class Solution(object):
    def findEvenNumbers(self, digits):
        count = [0] * 10
        for d in digits:
            count[d] += 1

        result = []
        for hundreds in range(1, 10):
            for tens in range(0, 10):
                for units in range(0, 10, 2):
                    used = [0] * 10
                    used[hundreds] += 1
                    used[tens] += 1
                    used[units] += 1

                    valid = True
                    for digit in range(10):
                        if used[digit] > count[digit]:
                            valid = False
                            break

                    if valid:
                        result.append(hundreds * 100 + tens * 10 + units)

        return result