class Solution(object):
    def groupAnagrams(self, strs):
        res={}
        for i in strs:
            if tuple(sorted(i)) not in res:
                res[tuple(sorted(i))]=[i]
            else:
                res[tuple(sorted(i))].append(i)

        return res.values()
        