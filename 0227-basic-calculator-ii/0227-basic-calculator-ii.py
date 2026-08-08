class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        op = '+'
        n = len(s)
        for i in range(n):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ') or i == n - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    prev = stack.pop()
                    stack.append(int(float(prev) / num))
                op = ch
                num = 0
        return sum(stack)