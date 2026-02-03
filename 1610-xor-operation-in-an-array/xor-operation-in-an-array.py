class Solution(object):
    def xorOperation(self, n, start):
        res=[]
        i=0
        while len(res)<n:
            res.append(start+2*i)
            i+=1
        result = 0
        for i in res:
            result^=i
        return result

        