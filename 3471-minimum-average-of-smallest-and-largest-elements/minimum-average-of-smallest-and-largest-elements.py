class Solution(object):
    def minimumAverage(self, nums):
        averages = []
        nums.sort()
        left = 0
        right = len(nums)-1
        while left<right:
            averages.append((nums[left]+nums[right])/2.0)
            left+=1
            right-=1
        return min(averages)        