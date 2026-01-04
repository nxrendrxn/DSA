class Solution(object):
    def hammingWeight(self, n):
        b=bin(n)[2:]
        return (str(b).count('1'))
        