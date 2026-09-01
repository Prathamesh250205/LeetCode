class Solution(object):
    def isValid(self, code):
        stack = []
        i = 0
        n = len(code)
        
        while i < n:
            if i > 0 and not stack:
                return False
            
            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False
                j = i + 9
                k = code.find("]]>", j)
                if k == -1:
                    return False
                i = k + 3
            elif code.startswith("</", i):
                j = i + 2
                k = code.find(">", j)
                if k == -1:
                    return False
                tag_name = code[j:k]
                if not stack or stack[-1] != tag_name:
                    return False
                stack.pop()
                i = k + 1
            elif code.startswith("<", i):
                j = i + 1
                k = code.find(">", j)
                if k == -1:
                    return False
                tag_name = code[j:k]
                if not (1 <= len(tag_name) <= 9 and tag_name.isupper() and tag_name.isalpha()):
                    return False
                stack.append(tag_name)
                i = k + 1
            else:
                i += 1
                
        return len(stack) == 0