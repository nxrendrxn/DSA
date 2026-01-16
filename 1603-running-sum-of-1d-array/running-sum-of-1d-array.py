class Solution(object):
    def runningSum(self, nums):
        p=[nums[0]]
        for i in range(1,len(nums)):
            p.append(p[i-1]+nums[i])
        return p
        