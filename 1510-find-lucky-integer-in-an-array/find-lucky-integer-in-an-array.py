class Solution(object):
    def findLucky(self, arr):
        s=set(arr)
        lucky=0
        for i in s:
            if arr.count(i)==i:
                if i>lucky:
                    lucky=i
        if lucky == 0:
            return -1
        return lucky
        