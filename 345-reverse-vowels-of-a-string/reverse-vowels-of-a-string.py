class Solution(object):
    def reverseVowels(self, s):
        v={'a','e','i','o','u','A','E','I','O','U'}
        res=[i for i in s]
        left=0
        right=len(s)-1
        while left<right:
            if res[left] not in v:
                left+=1
            elif res[right] not in v:
                right-=1
            elif res[right] in v and res[left] in v:
                res[right],res[left]=res[left],res[right]
                left+=1
                right-=1
        f="".join(res)
        return f
        

        
        