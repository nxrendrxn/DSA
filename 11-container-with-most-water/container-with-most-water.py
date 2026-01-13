class Solution(object):
    def maxArea(self, height):
        area = 0
        left = 0
        right = len(height)-1
        while left < right :
            current = min(height[left],height[right]) * (right-left)
            if current>area:
                area = current
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area