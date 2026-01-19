class Solution(object):
    def differenceOfSum(self, nums):
        element = sum(nums)
        digit = 0
        for i in nums:
            while i>0:
                digit += i%10
                i=i//10
        return abs(element - digit)
        