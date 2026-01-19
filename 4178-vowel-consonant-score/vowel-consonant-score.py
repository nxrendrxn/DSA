class Solution(object):
    def vowelConsonantScore(self, s):
        v = 0
        c = 0
        vow = {'a','e','i','o','u'}
        for i in s:
            if i.isalpha():
                if i in vow:
                    v+=1
                else:
                    c+=1
        if c>0:
            return v//c
        return 0
        