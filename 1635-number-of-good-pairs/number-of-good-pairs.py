class Solution(object):
    def numIdenticalPairs(self, nums):
        s=set(nums)
        hmap = {}
        for i in s:
            hmap[i]=nums.count(i)
        count = 0
        for i in hmap.values():
            count+=(i*(i-1)//2)
        return count