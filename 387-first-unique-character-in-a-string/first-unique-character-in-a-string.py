class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
