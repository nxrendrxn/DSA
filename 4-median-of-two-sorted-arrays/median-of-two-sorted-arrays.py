class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums1+nums2
        nums3.sort()
        l=len(nums3)
        m=0.0
        for i in range(l):
            if l%2==0:
                m=(nums3[(l/2)]+nums3[(l/2)-1])/2.0
            else:
                m=nums3[((l+1)/2)-1]
        return m
        