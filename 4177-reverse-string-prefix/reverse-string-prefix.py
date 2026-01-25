class Solution(object):
    def reversePrefix(self, s, k):
        res=s[k-1::-1]+s[k:]
        return res
        

        