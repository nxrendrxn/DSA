class Solution(object):
    def alternatingSum(self, nums):
        eSum = 0
        oSum = 0
        for i in range(len(nums)):
            if i%2==0:
                eSum+= nums[i]
            else:
                oSum+= nums[i]
        return eSum - oSum
        