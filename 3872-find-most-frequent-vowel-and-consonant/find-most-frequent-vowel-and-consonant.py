class Solution(object):
    def maxFreqSum(self, s):
        v={'a','e','i','o','u'}
        vSet={}
        cSet={}
        for i in s:
            if i in v:
                if i not in vSet:
                    vSet[i]=1
                else:
                    vSet[i]+=1
            else:
                if i not in cSet:
                    cSet[i]=1
                else:
                    cSet[i]+=1
        maxV = max(vSet.values()) if vSet else 0
        maxC = max(cSet.values()) if cSet else 0
        return (maxV+maxC)
        