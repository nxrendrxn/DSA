class Solution(object):
    def maxNumberOfBalloons(self, text):
        hmap = {}
        target = {'b', 'a', 'l', 'o', 'n'}
        res = []
        for i in text:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        for i in target:
            if i not in hmap:
                return 0
            if i == 'l' or i == 'o':
                res.append(hmap[i] // 2)
            else:
                res.append(hmap[i])

        return min(res)
