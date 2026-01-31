class Solution(object):
    def isValid(self, s):
        hmap = { '}':'{', ')':'(', ']':'[' }
        stack = []
        for i in s:
            if i not in hmap:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                elif stack[-1]==hmap.get(i):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True     
        