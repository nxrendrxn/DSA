class Solution(object):
    def xorOperation(self, n, start):
        res=[]
        i=0
        for i in range(0,n):
            res.append(start+2*i)
        result = 0
        for i in res:
            result^=i
        return result

        