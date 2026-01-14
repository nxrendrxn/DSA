class Solution(object):
    def twoSum(self, nums, target):
        hm={}
        res=[]
        for i in range(len(nums)):
            if target-nums[i] in hm:
                res.append(hm.get(target-nums[i]))
                res.append(i)
            else:
                hm[nums[i]]=i
        return res


        