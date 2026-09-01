class Solution(object):
    def deserialize(self, s):
        if not s:
            return None
        
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num = ""
        
        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c in ',]':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                if c == ']' and len(stack) > 1:
                    popped = stack.pop()
                    stack[-1].add(popped)
            else:
                num += c
                
        return stack[0]