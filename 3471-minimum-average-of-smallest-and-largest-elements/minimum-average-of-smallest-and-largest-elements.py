class Solution(object):
    def minimumAverage(self, nums):
        averages = []
        while len(nums)>1:
            averages.append((max(nums)+min(nums))/2.0)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(averages)        