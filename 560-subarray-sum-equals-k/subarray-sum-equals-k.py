class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        current = 0
        pmap = {0:1}
        for i in nums:
            current+=i
            if current-k in pmap:
                count+=pmap[current-k]
            pmap[current]=pmap.get(current,0)+1
        return count
        