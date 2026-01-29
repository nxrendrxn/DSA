class Solution(object):
    def isIsomorphic(self, s, t):
        hs = {}
        ht = {}
        for i in range(len(s)):
            if s[i] in hs:
                if hs[s[i]] != t[i]:
                    return False
            else:
                hs[s[i]] = t[i]

            if t[i] in ht:
                if ht[t[i]] != s[i]:
                    return False
            else:
                ht[t[i]] = s[i]
        return True
