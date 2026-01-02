class Solution(object):
    def isAnagram(self, s, t):
        ss=sorted(s)
        tt=sorted(t)
        if ss==tt:
            return True
        else:
            return False
        