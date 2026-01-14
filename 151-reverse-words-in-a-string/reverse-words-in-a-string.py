class Solution(object):
    def reverseWords(self, s):
        s=s.strip()
        l=s.split()
        left = 0
        right = len(l)-1
        while left<right:
            l[left],l[right]=l[right],l[left]
            left+=1
            right-=1
        res=" ".join(l)
        return res