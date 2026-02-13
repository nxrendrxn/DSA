class Solution:
    def firstMissingPositive(self, nums):
        s = set(num for num in nums if num > 0)
        i = 1
        while i in s:
            i += 1
        return i