class Solution(object):
    def isPalindrome(self, s):
        res=""
        for i in s:
            if i.isalpha() or i.isdigit():
                res+=i.lower()
        left = 0
        right = len(res)-1
        while left<right:
            if res[left]!=res[right]:
                return False
            left+=1
            right-=1
        return True
        