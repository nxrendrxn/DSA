class Solution(object):
    def singleNumber(self, nums):
        r=list(set(nums))
        a=[]
        for i in r:
            if nums.count(i)>1:
                continue
            else:
                a.append(i)
        return a 
        