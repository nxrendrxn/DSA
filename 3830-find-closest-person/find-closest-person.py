class Solution(object):
    def findClosest(self, x, y, z):
        xDistance = abs(z - x)
        yDistance = abs(z - y)
        if xDistance > yDistance :
            return 2
        elif xDistance < yDistance:
            return 1
        else:
            return 0
        